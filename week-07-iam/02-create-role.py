import boto3
import json

# Initialize the IAM client
iam = boto3.client('iam')

# Define the assume role policy document
assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}

try:
    # Create a new role
    role_response = iam.create_role(
        RoleName='just-jules-devops-role',
        AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
        Description='Role for EC2 to access S3'
    )
    print("Role created:", role_response['Role']['Arn'])

    # Attach policy to role
    iam.attach_role_policy(
        RoleName='just-jules-devops-role',
        PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
    )
    print("AmazonS3FullAccess policy attached to role.")
except Exception as e:
    print(f"Error creating role or attaching policy: {e}")
