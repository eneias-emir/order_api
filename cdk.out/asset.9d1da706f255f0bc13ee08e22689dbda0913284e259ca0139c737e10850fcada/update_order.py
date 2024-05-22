import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    order_id = event['pathParameters']['orderId']
    update_details = json.loads(event['body'])
    
    update_expression = "SET "
    expression_attribute_values = {}
    
    for key, value in update_details.items():
        update_expression += f"{key} = :{key}, "
        expression_attribute_values[f":{key}"] = value
    
    update_expression = update_expression.rstrip(", ")

    table.update_item(
        Key={'orderId': order_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order updated successfully!'})
    }
