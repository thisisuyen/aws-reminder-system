"""Temporary test target for EventBridge Scheduler (replace with Uyen's Send Lambda)."""
import json


def lambda_handler(event, context):
    print("SCHEDULER_TRIGGERED:", json.dumps({
        "reminderId": event.get("reminderId"),
        "title": event.get("title"),
    }, ensure_ascii=False))
    return {"ok": True, "reminderId": event.get("reminderId")}
