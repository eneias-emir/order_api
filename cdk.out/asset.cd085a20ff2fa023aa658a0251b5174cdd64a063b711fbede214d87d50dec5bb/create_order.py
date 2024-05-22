import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())
    order_details = json.loads(event['body'])
    order_details['orderId'] = order_id

    table.put_item(Item=order_details)
    
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Order created successfully!', 'orderId': order_id})
    }
