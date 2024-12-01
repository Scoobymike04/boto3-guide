import boto3

# Initialize the IAM client
iam = boto3.client('iam')

policy_arn = 'arn:aws:iam::011528298515:policy/just-jules-devops-ListBucketPolicy'
user_name = 'just-jules-devops'

try:
    # Detach the policy from the user
    iam.detach_user_policy(UserName=user_name, PolicyArn=policy_arn)
    print(f"Policy '{policy_arn}' detached from user '{user_name}'.")

    # Delete the policy
    iam.delete_policy(PolicyArn=policy_arn)
    print(f"Policy '{policy_arn}' deleted successfully.")
except Exception as e:
    print(f"Error detaching or deleting policy: {e}")
