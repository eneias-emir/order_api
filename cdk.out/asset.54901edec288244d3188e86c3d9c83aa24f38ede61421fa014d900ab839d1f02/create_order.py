import json
import boto3
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())
    order_details = json.loads(event['body'], parse_float=Decimal)
    order_details['orderId'] = order_id

    table.put_item(Item=order_details)
    
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Order created successfully!', 'orderId': order_id}, default=decimal_default)
    }
