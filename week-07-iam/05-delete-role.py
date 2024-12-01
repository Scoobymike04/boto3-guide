import boto3

# Initialize the IAM client
iam = boto3.client('iam')

role_name = 'just-jules-devops-role'

try:
    # Detach policies from the role
    iam.detach_role_policy(RoleName=role_name, PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')
    print("Detached AmazonS3FullAccess policy from role.")

    # Delete the IAM role
    response = iam.delete_role(RoleName=role_name)
    print("Role deleted:", role_name)
except Exception as e:
    print(f"Error deleting role: {e}")
