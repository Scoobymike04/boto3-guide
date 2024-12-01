import boto3
import json

# Initialize the IAM client
iam = boto3.client('iam')

# Create a new IAM policy
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example_bucket"
        }
    ]
}

try:
    response = iam.create_policy(
        PolicyName='just-jules-devops-ListBucketPolicy',
        PolicyDocument=json.dumps(policy_document)
    )
    policy_arn = response['Policy']['Arn']
    print("Policy created:", policy_arn)

    # Attach the policy to the user
    iam.attach_user_policy(UserName='just-jules-devops', PolicyArn=policy_arn)
    print("Policy attached to user.")
except Exception as e:
    print(f"Error creating or attaching policy: {e}")
