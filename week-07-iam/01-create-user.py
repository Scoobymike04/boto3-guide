import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# Create a new IAM user
try:
    response = iam.create_user(UserName='just-jules-devops')
    print("User created:", response['User']['UserName'])
except Exception as e:
    print(f"Error creating user: {e}")
