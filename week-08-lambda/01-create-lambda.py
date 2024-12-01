import boto3
import json

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Read the zipped Lambda code
with open('lambda_function.zip', 'rb') as f:
    zipped_code = f.read()

# Create a new Lambda function
response = lambda_client.create_function(
    FunctionName='my_lambda_function',
    Runtime='python3.8',
    Role='arn:aws:iam::011528298515:role/sunday-lambda',  # Replace with your actual role ARN
    Handler='lambda_function.lambda_handler',  # lambda_function.py with the handler function
    Code=dict(ZipFile=zipped_code),
    Timeout=300,  # 5 minutes
    MemorySize=128
)

print("Lambda function created:", response['FunctionArn'])