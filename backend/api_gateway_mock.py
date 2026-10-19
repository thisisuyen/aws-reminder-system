"""Temporary POST /reminders mock for Uyen's separate Learner Lab account.

DO NOT use as the final backend. Use Van's reminder-create-api in the primary account.
"""

import json


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "POST")
    if method != "POST":
        return {"statusCode": 405, "body": json.dumps({"message": "Use POST"})}

    try:
        data = json.loads(event.get("body") or "{}")
        if not data.get("title") or not data.get("reminderTime") or not data.get("email"):
            raise ValueError("Missing title, reminderTime or email")
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "API Gateway connected to mock", "status": "MOCK_ONLY"}),
        }
    except (json.JSONDecodeError, ValueError) as error:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": str(error)}),
        }
