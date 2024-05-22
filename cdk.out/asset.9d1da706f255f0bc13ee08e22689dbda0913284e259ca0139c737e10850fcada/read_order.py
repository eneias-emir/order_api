# lambda/read_order.py
import json
import boto3
from utils import decimal_default

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    order_id = event['pathParameters']['orderId']
    
    response = table.get_item(Key={'orderId': order_id})
    
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'], default=decimal_default)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Order not found'})
        }
