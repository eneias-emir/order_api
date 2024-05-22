import aws_cdk as cdk
from orders_api.orders_api_stack import OrdersApiStack

app = cdk.App()
env = cdk.Environment(account="616048412683", region="us-east-2")
OrdersApiStack(app, "OrdersApiStack", env=env)

app.synth()

