import aws_cdk as core
import aws_cdk.assertions as assertions

from orders_api.orders_api_stack import OrdersApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in orders_api/orders_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = OrdersApiStack(app, "orders-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
