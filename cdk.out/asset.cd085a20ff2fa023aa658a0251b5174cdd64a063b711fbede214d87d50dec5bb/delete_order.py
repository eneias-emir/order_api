import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    order_id = event['pathParameters']['orderId']
    
    table.delete_item(Key={'orderId': order_id})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order deleted successfully!'})
    }
