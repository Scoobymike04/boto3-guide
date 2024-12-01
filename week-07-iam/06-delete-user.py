import boto3

# Initialize the IAM client
iam = boto3.client('iam')

user_name = 'just-jules-devops'

try:
    # Delete an IAM user
    iam.delete_user(UserName=user_name)
    print(f"User '{user_name}' deleted.")
except Exception as e:
    print(f"Error deleting user: {e}")
