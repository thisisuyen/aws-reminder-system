"""Week 3 - GET /reminders (AWS HTTP API -> Lambda -> DynamoDB).

Small classroom demonstration: scan up to MAX_ITEMS; for production, replace
scan with an authenticated and properly indexed per-user query.
"""
import json
import os
from decimal import Decimal

import boto3
from botocore.exceptions import ClientError

TABLE_NAME = os.environ.get("TABLE_NAME", "Reminders")
MAX_ITEMS = int(os.environ.get("MAX_ITEMS", "500"))
table = boto3.resource("dynamodb").Table(TABLE_NAME)


def reply(code, payload):
    return {
        "statusCode": code,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps(payload, ensure_ascii=False, default=lambda x: float(x) if isinstance(x, Decimal) else str(x)),
    }


def lambda_handler(event, context):
    method = (event.get("requestContext", {}).get("http", {}).get("method")
              or event.get("httpMethod") or "GET")
    if method != "GET":
        return reply(405, {"message": "Method not allowed"})
    items = []
    args = {}
    try:
        while True:
            result = table.scan(**args)
            items.extend(result.get("Items", []))
            last_key = result.get("LastEvaluatedKey")
            if not last_key or len(items) >= MAX_ITEMS:
                break
            args["ExclusiveStartKey"] = last_key
        items.sort(key=lambda item: item.get("createdAt", ""), reverse=True)
        limited = items[:MAX_ITEMS]
        return reply(200, {
            "items": limited,
            "count": len(limited),
            "truncated": bool(last_key or len(items) > MAX_ITEMS),
        })
    except ClientError as exc:
        print("GET_REMINDERS_ERROR", exc.response.get("Error", {}).get("Code", "Unknown"))
        return reply(500, {"message": "Cannot load reminders"})
