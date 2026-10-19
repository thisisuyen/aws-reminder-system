"""EventBridge Scheduler -> Lambda Send -> Amazon SNS (Week 2).

Scheduler target input from Van's create_reminder.py:
{"reminderId": "R-...", "title": "...", "description": "...", "email": "..."}

SNS Topic delivers to its confirmed subscriptions, NOT dynamically to event['email'].
"""

import os
import boto3

sns = boto3.client("sns", region_name=os.getenv("AWS_REGION", "us-east-1"))


def lambda_handler(event, context):
    if not isinstance(event, dict):
        raise ValueError("Scheduler input must be a JSON object")

    reminder_id = str(event.get("reminderId", "")).strip()
    title = str(event.get("title", "")).strip()
    description = str(event.get("description", "")).strip()

    if not reminder_id or not title:
        raise ValueError("reminderId and title are required")

    topic_arn = os.environ["SNS_TOPIC_ARN"]
    subject = "Nhac viec: " + " ".join(title.split())[:75]
    message = (
        "HE THONG NHAC VIEC - NHOM SERVERLESS\n\n"
        f"Tieu de: {title}\n"
        f"Noi dung: {description or '(khong co)'}\n"
        f"Ma loi nhac: {reminder_id}\n"
    )

    result = sns.publish(TopicArn=topic_arn, Subject=subject, Message=message)
    message_id = result["MessageId"]
    print(f"SNS_PUBLISH_SUCCESS reminderId={reminder_id} messageId={message_id}")
    return {"ok": True, "reminderId": reminder_id, "snsMessageId": message_id}
