"""Lambda POST /reminders for the AWS Reminder System (Week 2)."""

import json
import os
import re
import uuid
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import boto3
from botocore.exceptions import ClientError

VN_TZ = ZoneInfo("Asia/Ho_Chi_Minh")
TABLE_NAME = os.environ["TABLE_NAME"]
SCHEDULER_GROUP = os.environ["SCHEDULER_GROUP"]
SCHEDULER_ROLE_ARN = os.environ["SCHEDULER_ROLE_ARN"]
TARGET_LAMBDA_ARN = os.environ["TARGET_LAMBDA_ARN"]

table = boto3.resource("dynamodb").Table(TABLE_NAME)
scheduler = boto3.client("scheduler")


def reply(code, data):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*",  # Demo; restrict to frontend origin later.
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST,OPTIONS",
        },
        "body": json.dumps(data, ensure_ascii=False),
    }


def lambda_handler(event, context):
    method = (
        event.get("requestContext", {}).get("http", {}).get("method")
        or event.get("httpMethod")
        or "POST"
    )
    if method == "OPTIONS":
        return reply(200, {"message": "OK"})
    if method != "POST":
        return reply(405, {"message": "Method not allowed"})

    try:
        raw_body = event.get("body", event)
        data = json.loads(raw_body) if isinstance(raw_body, str) else raw_body
        if not isinstance(data, dict):
            raise ValueError("JSON body must be an object")

        title = str(data.get("title", "")).strip()
        email = str(data.get("email", "")).strip()
        description = str(data.get("description", "")).strip()
        time_text = str(data.get("reminderTime", "")).strip()

        if not title or len(title) > 200:
            raise ValueError("title is required and must be <= 200 characters")
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
            raise ValueError("email is invalid")
        if not time_text:
            raise ValueError("reminderTime is required")

        reminder_dt = datetime.fromisoformat(time_text.replace("Z", "+00:00"))
        if reminder_dt.tzinfo is None:
            raise ValueError("reminderTime must include a timezone offset")
        if reminder_dt.astimezone(timezone.utc) <= datetime.now(timezone.utc) + timedelta(minutes=2):
            raise ValueError("reminderTime must be more than 2 minutes in the future")

    except (ValueError, TypeError, json.JSONDecodeError) as exc:
        return reply(400, {"message": str(exc)})

    reminder_id = "R-" + uuid.uuid4().hex[:16]
    schedule_name = "reminder-" + reminder_id
    vn_time = reminder_dt.astimezone(VN_TZ)
    created_at = datetime.now(VN_TZ).isoformat(timespec="seconds")

    item = {
        "reminderId": reminder_id,
        "title": title,
        "description": description,
        "email": email,
        "reminderTime": reminder_dt.isoformat(timespec="seconds"),
        "status": "PENDING",
        "scheduleName": schedule_name,
        "createdAt": created_at,
    }

    try:
        table.put_item(Item=item, ConditionExpression="attribute_not_exists(reminderId)")
    except ClientError as exc:
        print("DynamoDB PutItem failed:", exc.response["Error"]["Code"])
        return reply(500, {"message": "Failed to save reminder"})

    target_event = {
        "reminderId": reminder_id,
        "title": title,
        "description": description,
        "email": email,
    }

    try:
        created_schedule = scheduler.create_schedule(
            Name=schedule_name,
            GroupName=SCHEDULER_GROUP,
            ScheduleExpression=f"at({vn_time.strftime('%Y-%m-%dT%H:%M:%S')})",
            ScheduleExpressionTimezone="Asia/Ho_Chi_Minh",
            FlexibleTimeWindow={"Mode": "OFF"},
            ActionAfterCompletion="DELETE",
            State="ENABLED",
            Target={
                "Arn": TARGET_LAMBDA_ARN,
                "RoleArn": SCHEDULER_ROLE_ARN,
                "Input": json.dumps(target_event, ensure_ascii=False),
            },
        )
    except ClientError as exc:
        print("CreateSchedule failed:", exc.response["Error"]["Code"])
        try:
            table.update_item(
                Key={"reminderId": reminder_id},
                UpdateExpression="SET #state = :failed",
                ExpressionAttributeNames={"#state": "status"},
                ExpressionAttributeValues={":failed": "SCHEDULE_FAILED"},
            )
        except ClientError as update_exc:
            print("Failed to update reminder status:", update_exc.response["Error"]["Code"])
        return reply(500, {"message": "Reminder saved, but schedule creation failed", "reminderId": reminder_id})

    return reply(201, {
        "message": "Reminder created",
        "reminderId": reminder_id,
        "status": "PENDING",
        "scheduleName": schedule_name,
        "scheduleArn": created_schedule["ScheduleArn"],
    })
