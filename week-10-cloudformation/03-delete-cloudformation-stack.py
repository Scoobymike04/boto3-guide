import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation')

# Delete the CloudFormation stack
try:
    cloudformation.delete_stack(StackName='my-stack')
    print("CloudFormation stack deletion initiated.")
except Exception as e:
    print(f"Error deleting CloudFormation stack: {e}")
