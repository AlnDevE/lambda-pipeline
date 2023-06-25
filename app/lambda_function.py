from app.src.soma import soma


def lambda_handler(event, context):
    num1 = event["body"]["num1"]
    num2 = event["body"]["num2"]
    return soma(num1=num1, num2=num2)
