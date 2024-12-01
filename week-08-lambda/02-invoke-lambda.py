import boto3
import json

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName='my_lambda_function',
    InvocationType='RequestResponse',
    Payload=json.dumps({'key': 'value'})
)

# Print the response from the Lambda function
print("Lambda function response:", response['Payload'].read().decode('utf-8'))