"""Local smoke tests with fake AWS resources (no network/AWS credentials)."""
import importlib.util
import json
import os
from pathlib import Path

import pytest
from botocore.exceptions import ClientError

ROOT = Path(__file__).resolve().parent.parent / 'backend'


def aws_error(code):
    return ClientError({'Error': {'Code': code, 'Message': code}}, 'Test')


class FakeTable:
    def __init__(self):
        self.items = {}
        self.calls = []
    def scan(self, **kwargs):
        return {'Items': list(self.items.values())}
    def get_item(self, Key, **kwargs):
        i = self.items.get(Key['reminderId'])
        return {'Item': i.copy()} if i else {}
    def update_item(self, Key, UpdateExpression, ConditionExpression=None, ExpressionAttributeValues=None,
                    ExpressionAttributeNames=None, ReturnValues=None, **kwargs):
        key = Key['reminderId']
        item = self.items.get(key)
        vals = ExpressionAttributeValues or {}
        if ConditionExpression and (not item or item['status'] != vals.get(':pending', vals.get(':sending', item.get('status')))):
            raise aws_error('ConditionalCheckFailedException')
        if not item: raise aws_error('ResourceNotFoundException')
        if ':cancelled' in vals: item['status'] = 'CANCELLED'
        if ':sending' in vals and ':pending' in vals: item['status'] = 'SENDING'
        if ':sent' in vals: item['status'] = 'SENT'; item['sentAt'] = vals[':now']; item['snsMessageId']=vals[':msgid']
        if ':failed' in vals: item['status'] = 'SEND_FAILED'
        self.calls.append(('update', key, item['status']))
        return {'Attributes': item.copy()}
    def delete_item(self, Key, ExpressionAttributeValues, **kwargs):
        key=Key['reminderId']
        if key not in self.items or self.items[key]['status'] != ExpressionAttributeValues[':expected']:
            raise aws_error('ConditionalCheckFailedException')
        self.items.pop(key)
        self.calls.append(('delete', key))


class FakeScheduler:
    def __init__(self): self.deleted = []
    def delete_schedule(self, Name, GroupName): self.deleted.append((Name, GroupName))


class FakeSns:
    def __init__(self): self.published = []
    def publish(self, **kwargs):
        self.published.append(kwargs)
        return {'MessageId': 'MSG-TEST-1'}


@pytest.fixture
def setup_aws(monkeypatch):
    import boto3
    table = FakeTable(); scheduler=FakeScheduler(); sns=FakeSns()
    monkeypatch.setattr(boto3, 'resource', lambda service: type('R', (), {'Table': lambda _self, _name: table})())
    monkeypatch.setattr(boto3, 'client', lambda service, **kwargs: scheduler if service=='scheduler' else sns)
    monkeypatch.setenv('TABLE_NAME','Reminders')
    monkeypatch.setenv('SCHEDULER_GROUP','reminder-week2')
    monkeypatch.setenv('SNS_TOPIC_ARN','arn:aws:sns:us-east-1:111111111111:test')
    return table,scheduler,sns


def load_module(filename):
    spec=importlib.util.spec_from_file_location(filename.replace('.py',''), ROOT/filename)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def reminder(id='R-1234567890abcdef'):
    return dict(reminderId=id,title='Bai test',description='test',status='PENDING',
                scheduleName='reminder-'+id,createdAt='2026-10-22T10:00:00+07:00')


def test_get_and_delete_pending(setup_aws):
    table,scheduler,sns=setup_aws
    table.items['R-1234567890abcdef']=reminder()
    get=load_module('get_reminders.py')
    out=get.lambda_handler({'requestContext':{'http':{'method':'GET'}}},None)
    assert out['statusCode']==200
    assert json.loads(out['body'])['items'][0]['reminderId']=='R-1234567890abcdef'
    delete=load_module('delete_reminder.py')
    event={'requestContext':{'http':{'method':'DELETE'}},'pathParameters':{'id':'R-1234567890abcdef'}}
    out=delete.lambda_handler(event,None)
    assert out['statusCode']==200
    assert 'R-1234567890abcdef' not in table.items
    assert scheduler.deleted==[('reminder-R-1234567890abcdef','reminder-week2')]
    assert delete.lambda_handler(event,None)['statusCode']==404


def test_send_once_and_skip_duplicate(setup_aws):
    table,scheduler,sns=setup_aws
    table.items['R-1234567890abcdef']=reminder()
    send=load_module('send_reminder.py')
    event={'reminderId':'R-1234567890abcdef'}
    first=send.lambda_handler(event,None)
    assert first['status']=='SENT'
    assert table.items['R-1234567890abcdef']['status']=='SENT'
    assert len(sns.published)==1
    second=send.lambda_handler(event,None)
    assert second['skipped'] is True
    assert len(sns.published)==1


def test_cancelled_reminder_cannot_send(setup_aws):
    table,scheduler,sns=setup_aws
    table.items['R-1234567890abcdef']=reminder()
    table.items['R-1234567890abcdef']['status']='CANCELLED'
    send=load_module('send_reminder.py')
    out=send.lambda_handler({'reminderId':'R-1234567890abcdef'},None)
    assert out['skipped'] is True
    assert not sns.published
