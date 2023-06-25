from app.src.soma import soma
import json


def lambda_handler(event, context):
    body = json.loads(event["body"])
    num1 = body["num1"]
    num2 = body["num2"]
    return soma(num1=num1, num2=num2)
