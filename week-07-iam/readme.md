Managing IAM Users and Roles with AWS GUI and Boto3

Learn how to create, modify, delete, and manage IAM users and roles using both the AWS Management Console (GUI) and Boto3 (Python SDK).

Part 1: Managing IAM Users and Roles with AWS GUI
Creating an IAM User
- Log in to the AWS Management Console.
- Navigate to the IAM service by searching for "IAM" in the search bar.
- Select Users from the left-hand menu and click Add user.
- Configure the user's details:
    User name: Enter a unique username (e.g., new_user).
    Access type: Choose programmatic access, console access, or both.
- Assign permissions:
    Select predefined AWS policies (e.g., AdministratorAccess).
    Add the user to existing IAM groups.
    Attach custom policies if needed.
- Add optional tags for identification and click Next: Review.
- Review the user details and click Create user.
- If programmatic access is enabled, download the credentials (Access Key ID and Secret Access Key).

Modifying IAM User Permissions
- Go to Users in the IAM Dashboard.
- Click the username of the user to modify.
- Under the Permissions tab:
    Attach or detach policies.
    Add or remove the user from IAM groups.
- Save changes.

Deleting an IAM User
- Navigate to Users in the IAM Dashboard.
- Select the user to delete.
- Click Delete user and confirm the deletion.

Creating an IAM Role
- Log in to the AWS Management Console and go to the IAM service.
- Select Roles and click Create role.
- Choose the trusted entity (e.g., AWS service like EC2 or Lambda).
- Attach required policies (e.g., AmazonS3FullAccess).
- Add optional tags for identification.
- Review the role details and click Create role.

Modifying and Deleting IAM Roles
- Go to Roles in the IAM Dashboard.
- Select the role to modify or delete.
- Modify permissions under the Permissions tab as needed.
- To delete the role, click Delete and confirm.

Part 2: Managing IAM Users and Roles with Boto3
Prerequisites
Install Boto3: pip install boto3
Configure AWS CLI: aws configure
Creating an IAM User with Boto3

import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# Create a new IAM user
response = iam.create_user(UserName='new_user')
print("User created:", response['User']['UserName'])
Attaching a Policy to a User with Boto3

import boto3
import json

# Initialize the IAM client
iam = boto3.client('iam')

# Create a new policy
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

response = iam.create_policy(
    PolicyName='ListBucketPolicy',
    PolicyDocument=json.dumps(policy_document)
)
policy_arn = response['Policy']['Arn']
print("Policy created:", policy_arn)

# Attach the policy to the user
iam.attach_user_policy(UserName='new_user', PolicyArn=policy_arn)
print("Policy attached to user.")
Deleting an IAM User with Boto3

import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# Delete an IAM user
response = iam.delete_user(UserName='new_user')
print("User deleted.")
Creating an IAM Role with Boto3

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

# Create a new role
role_response = iam.create_role(
    RoleName='my_role',
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
    Description='Role for EC2 to access S3'
)
print("Role created:", role_response['Role']['Arn'])

# Attach a policy to the role
iam.attach_role_policy(
    RoleName='my_role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)
print("Policy attached to role.")
Deleting an IAM Role with Boto3

import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# Detach policies from the role
iam.detach_role_policy(RoleName='my_role', PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')

# Delete the IAM role
response = iam.delete_role(RoleName='my_role')
print("Role deleted.")

Summary
This lesson covered the following:
- Using the AWS Management Console to create, modify, and delete IAM users and roles.
- Automating IAM management with Boto3, including scripts to create, attach policies, and delete users and roles.
