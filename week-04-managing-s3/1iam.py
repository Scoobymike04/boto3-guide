import boto3
import json

# Define the policy document
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:PutObject",
                "s3:GetObject",
                "s3:PutBucketNotification",
                "s3:PutBucketLogging",
                "s3:CopyObject"
            ],
            "Resource": "arn:aws:s3:::*"
        },
    ]
}

# Initialize the IAM client
iam = boto3.client('iam')

# Create the policy
policy_name = 'S3OperationsPolicy'
try:
    response = iam.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)
    )
    policy_arn = response['Policy']['Arn']
    print(f"Policy '{policy_name}' created successfully with ARN: {policy_arn}")
except iam.exceptions.EntityAlreadyExistsException:
    policy_arn = f"arn:aws:iam::891376916144:policy/{policy_name}"
    print(f"Policy '{policy_name}' already exists with ARN: {policy_arn}")
except Exception as e:
    print(f"Error creating policy: {e}")

# Attach the policy to a user
user_name = 'alexboto'
try:
    iam.attach_user_policy(
        UserName=user_name,
        PolicyArn=policy_arn
    )
    print(f"Policy '{policy_name}' attached to user '{user_name}' successfully.")
except Exception as e:
    print(f"Error attaching policy: {e}")