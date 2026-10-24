"""Week 3 - Scheduler -> Lambda Send -> SNS + DynamoDB SENT.

For this classroom demo, SENT means SNS accepted a Publish request, not
confirmed delivery to the recipient's mailbox. Conditional state changes
avoid double-publishing if Scheduler invokes the same reminder twice.
"""
import os
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

sns = boto3.client("sns")
table = boto3.resource("dynamodb").Table(os.environ.get("TABLE_NAME", "Reminders"))


def lambda_handler(event, context):
    if not isinstance(event, dict):
        raise ValueError("Scheduler input must be a JSON object")
    reminder_id = str(event.get("reminderId", "")).strip()
    if not reminder_id:
        raise ValueError("reminderId is required")

    # Claim PENDING atomically. CANCELLED/SENT/SENDING won't publish.
    try:
        item = table.update_item(
            Key={"reminderId": reminder_id},
            UpdateExpression="SET #s = :sending",
            ConditionExpression="attribute_exists(reminderId) AND #s = :pending",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":sending": "SENDING", ":pending": "PENDING"},
            ReturnValues="ALL_NEW",
        )["Attributes"]
    except ClientError as exc:
        if exc.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
            print("SNS_SKIPPED_NOT_PENDING", reminder_id)
            return {"ok": False, "skipped": True, "reminderId": reminder_id}
        print("DYNAMODB_CLAIM_ERROR", exc.response.get("Error", {}).get("Code", "Unknown"))
        raise

    title = str(item.get("title", "")).strip()
    description = str(item.get("description", "")).strip()
    if not title:
        print("MISSING_TITLE_FOR_SEND", reminder_id)
        table.update_item(
            Key={"reminderId": reminder_id},
            UpdateExpression="SET #s = :failed",
            ConditionExpression="#s = :sending",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":failed": "SEND_FAILED", ":sending": "SENDING"},
        )
        raise ValueError("title missing in stored reminder")

    subject = "Nhac viec: " + " ".join(title.split())[:75]
    message = (
        "HE THONG NHAC VIEC - NHOM SERVERLESS\n\n"
        f"Tieu de: {title}\n"
        f"Noi dung: {description or '(khong co)'}\n"
        f"Ma loi nhac: {reminder_id}\n"
    )
    try:
        result = sns.publish(TopicArn=os.environ["SNS_TOPIC_ARN"], Subject=subject, Message=message)
    except (ClientError, KeyError) as exc:
        print("SNS_PUBLISH_ERROR", reminder_id, str(exc)[:160])
        # No message accepted by SNS (or missing topic setting).
        try:
            table.update_item(
                Key={"reminderId": reminder_id},
                UpdateExpression="SET #s = :failed",
                ConditionExpression="#s = :sending",
                ExpressionAttributeNames={"#s": "status"},
                ExpressionAttributeValues={":failed": "SEND_FAILED", ":sending": "SENDING"},
            )
        except ClientError as update_exc:
            print("FAILED_TO_SET_SEND_FAILED", update_exc.response.get("Error", {}).get("Code"))
        raise

    message_id = result["MessageId"]
    # If this write fails, leave SENDING for manual review. Automatic retry
    # must NOT publish again because SNS already accepted the first request.
    table.update_item(
        Key={"reminderId": reminder_id},
        UpdateExpression="SET #s = :sent, sentAt = :now, snsMessageId = :msgid",
        ConditionExpression="#s = :sending",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={
            ":sent": "SENT", ":sending": "SENDING",
            ":now": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            ":msgid": message_id,
        },
    )
    print("SNS_PUBLISH_SUCCESS", reminder_id, message_id)
    print("DYNAMODB_STATUS_SENT", reminder_id)
    return {"ok": True, "reminderId": reminder_id, "snsMessageId": message_id, "status": "SENT"}
