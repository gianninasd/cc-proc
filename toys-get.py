import os
import json
import boto3
import decimal


# used to convert decimal values to a string
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


# A Lambda function that processes the test payload
def lambda_handler(event, context):
    print('toys-get received event, invoked by {}'.format(context.invoked_function_arn))
    # json_region = os.environ['AWS_REGION']

    dynamodb = boto3.resource('dynamodb')
    toys = dynamodb.Table('toys')
    data = toys.scan()
    items = data['Items']
    print('all rows: {}'.format(items))

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(items, cls=DecimalEncoder)
    }
