from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigatewayv2 as apigatewayv2,
    aws_apigatewayv2_integrations as integrations,
)
from constructs import Construct

class OrdersApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB table
        table = dynamodb.Table(self, "OrdersTable",
                               partition_key={"name": "orderId", "type": dynamodb.AttributeType.STRING},
                               table_name="Orders")

        # Lambda functions
        create_order_lambda = lambda_.Function(self, "CreateOrderFunction",
                                               runtime=lambda_.Runtime.PYTHON_3_8,
                                               handler="create_order.lambda_handler",
                                               code=lambda_.Code.from_asset("lambda"))

        read_order_lambda = lambda_.Function(self, "ReadOrderFunction",
                                             runtime=lambda_.Runtime.PYTHON_3_8,
                                             handler="read_order.lambda_handler",
                                             code=lambda_.Code.from_asset("lambda"))

        update_order_lambda = lambda_.Function(self, "UpdateOrderFunction",
                                               runtime=lambda_.Runtime.PYTHON_3_8,
                                               handler="update_order.lambda_handler",
                                               code=lambda_.Code.from_asset("lambda"))

        delete_order_lambda = lambda_.Function(self, "DeleteOrderFunction",
                                               runtime=lambda_.Runtime.PYTHON_3_8,
                                               handler="delete_order.lambda_handler",
                                               code=lambda_.Code.from_asset("lambda"))

        # Grant Lambda functions access to the DynamoDB table
        table.grant_read_write_data(create_order_lambda)
        table.grant_read_write_data(read_order_lambda)
        table.grant_read_write_data(update_order_lambda)
        table.grant_read_write_data(delete_order_lambda)

        # HTTP API Gateway
        http_api = apigatewayv2.HttpApi(self, "OrdersApi")

        # Define API integrations
        create_order_integration = integrations.LambdaProxyIntegration(handler=create_order_lambda)
        read_order_integration = integrations.LambdaProxyIntegration(handler=read_order_lambda)
        update_order_integration = integrations.LambdaProxyIntegration(handler=update_order_lambda)
        delete_order_integration = integrations.LambdaProxyIntegration(handler=delete_order_lambda)

        # Add routes to HTTP API
        http_api.add_routes(
            path="/orders",
            methods=[apigatewayv2.HttpMethod.POST],
            integration=create_order_integration,
        )

        http_api.add_routes(
            path="/orders/{orderId}",
            methods=[apigatewayv2.HttpMethod.GET],
            integration=read_order_integration,
        )

        http_api.add_routes(
            path="/orders/{orderId}",
            methods=[apigatewayv2.HttpMethod.PUT],
            integration=update_order_integration,
        )

        http_api.add_routes(
            path="/orders/{orderId}",
            methods=[apigatewayv2.HttpMethod.DELETE],
            integration=delete_order_integration,
        )
