"""Week 3 - DELETE /reminders/{id}.

Pending reminders: mark CANCELLED first, remove Scheduler, then delete item.
Sent/failed reminders: delete the stored item (already terminal status).
Never remove a SENDING reminder; it may already have published to SNS.
"""
import json
import os
import re
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

TABLE_NAME = os.environ.get("TABLE_NAME", "Reminders")
SCHEDULER_GROUP = os.environ.get("SCHEDULER_GROUP", "reminder-week2")
table = boto3.resource("dynamodb").Table(TABLE_NAME)
scheduler = boto3.client("scheduler")


def reply(code, payload):
    return {
        "statusCode": code,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps(payload, ensure_ascii=False),
    }


def lambda_handler(event, context):
    method = (event.get("requestContext", {}).get("http", {}).get("method")
              or event.get("httpMethod") or "DELETE")
    if method != "DELETE":
        return reply(405, {"message": "Method not allowed"})
    reminder_id = (event.get("pathParameters") or {}).get("id", "")
    if not re.fullmatch(r"R-[a-zA-Z0-9-]{5,64}", reminder_id):
        return reply(400, {"message": "Invalid reminderId"})

    try:
        response = table.get_item(Key={"reminderId": reminder_id}, ConsistentRead=True)
        item = response.get("Item")
        if not item:
            return reply(404, {"message": "Reminder not found", "reminderId": reminder_id})

        current_status = item.get("status")
        if current_status == "SENDING":
            return reply(409, {"message": "Reminder is currently sending; cannot delete", "reminderId": reminder_id})
        if current_status not in ("PENDING", "CANCELLED", "SENT", "SEND_FAILED", "SCHEDULE_FAILED"):
            return reply(409, {"message": f"Cannot delete status {current_status}", "reminderId": reminder_id})
        if current_status in ("PENDING", "CANCELLED"):
            if current_status == "PENDING":
                # Lock cancellation before Scheduler removal; Lambda Send may
                # only claim status=PENDING. If send already claimed, fail 409.
                try:
                    table.update_item(
                        Key={"reminderId": reminder_id},
                        UpdateExpression="SET #s = :cancelled, cancelledAt = :now",
                        ConditionExpression="#s = :pending",
                        ExpressionAttributeNames={"#s": "status"},
                        ExpressionAttributeValues={
                            ":pending": "PENDING", ":cancelled": "CANCELLED",
                            ":now": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        },
                    )
                except ClientError as exc:
                    if exc.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
                        return reply(409, {"message": "Status changed; refresh and retry", "reminderId": reminder_id})
                    raise
            schedule_name = item.get("scheduleName")
            if not schedule_name:
                return reply(500, {"message": "Marked CANCELLED, but scheduleName missing; check manually", "reminderId": reminder_id})
            try:
                scheduler.delete_schedule(Name=schedule_name, GroupName=SCHEDULER_GROUP)
                print("SCHEDULE_DELETED", reminder_id)
            except ClientError as exc:
                code = exc.response.get("Error", {}).get("Code", "Unknown")
                if code != "ResourceNotFoundException":
                    print("DELETE_SCHEDULE_ERROR", reminder_id, code)
                    return reply(500, {"message": "Marked CANCELLED but Scheduler deletion failed; retry DELETE", "reminderId": reminder_id})
                print("SCHEDULE_ALREADY_MISSING", reminder_id)
            expected_status = "CANCELLED"
        else:
            # SENT, SEND_FAILED, SCHEDULE_FAILED have no pending schedule to
            # cancel in the normal workflow. If unexpectedly present, inspect
            # the AWS Scheduler console rather than silently assuming.
            expected_status = current_status

        try:
            table.delete_item(
                Key={"reminderId": reminder_id},
                ConditionExpression="#s = :expected",
                ExpressionAttributeNames={"#s": "status"},
                ExpressionAttributeValues={":expected": expected_status},
            )
        except ClientError as exc:
            if exc.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
                return reply(409, {"message": "Status changed; refresh and retry", "reminderId": reminder_id})
            raise
        print("REMINDER_DELETED", reminder_id, current_status)
        return reply(200, {"message": "Reminder deleted", "reminderId": reminder_id, "status": "DELETED"})
    except ClientError as exc:
        print("DELETE_REMINDER_ERROR", exc.response.get("Error", {}).get("Code", "Unknown"))
        return reply(500, {"message": "Cannot cancel reminder", "reminderId": reminder_id})
