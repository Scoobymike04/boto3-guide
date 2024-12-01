import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation')

# View the CloudFormation stack details
try:
    response = cloudformation.describe_stacks(StackName='my-stack')
    stack_details = response['Stacks'][0]
    print("CloudFormation Stack Details:")
    print(f"Stack Name: {stack_details['StackName']}")
    print(f"Stack Status: {stack_details['StackStatus']}")
    print(f"Creation Time: {stack_details['CreationTime']}")
    print(f"Stack Outputs: {stack_details.get('Outputs', 'No Outputs')}")
except Exception as e:
    print(f"Error retrieving CloudFormation stack details: {e}")
