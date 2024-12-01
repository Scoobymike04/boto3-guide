Managing AWS CloudFormation Stacks with AWS GUI and Boto3

Learn how to create, configure, and delete AWS CloudFormation stacks using both the AWS Management Console and Boto3.

What is AWS CloudFormation?
AWS CloudFormation is a service that helps you automate the creation, management, and provisioning of AWS infrastructure. Instead of manually setting up resources like servers, databases, and networking components, you define everything in a template (JSON or YAML). AWS CloudFormation then uses this template to provision and manage the resources for you.

How CloudFormation Works
- Template Creation: Define resources in a CloudFormation template using JSON or YAML.
- Stack Creation: Use the template to create a stack, which provisions all the defined resources.
- Management: Update the stack to modify resources or delete it to clean up all resources.

Why Use CloudFormation?
- Automation: Streamlines infrastructure provisioning and management.
- Scalability: Suitable for both small applications and complex enterprise systems.
- Consistency: Ensures resources are configured the same way every time.
- Flexibility: Integrates with other AWS services for powerful automation.

Part 1: Managing CloudFormation Stacks with the AWS GUI
Creating a CloudFormation Stack
- Log in to the AWS Management Console:
- Visit the AWS Management Console and log in with your credentials.
- Navigate to CloudFormation:
- Search for "CloudFormation" in the services search bar and select it.

Create a New Stack:
- Click Create stack.
- Select With new resources (standard).
- Choose Upload a template file, then upload your template.yaml.
- Click Next.

Configure Stack Details:
- Provide a stack name (e.g., my-stack).
- Add parameters as required by the template (e.g., InstanceType as t2.micro).
- Click Next.

Configure Options:
- Add optional settings like tags and permissions.
- Click Next.

Review and Create:
- Review the configuration.
- Acknowledge IAM resources if applicable.
- Click Create stack.
Outcome: The stack is created, and resources are provisioned as defined in the template.

Deleting a CloudFormation Stack
Navigate to CloudFormation:
- Open the CloudFormation dashboard in the AWS Management Console.

Delete the Stack:
- Select the stack you want to delete.
- Click Delete.
- Confirm the deletion.
Outcome: The stack and its associated resources are deleted.

Part 2: Managing CloudFormation Stacks with Boto3
Prerequisites
Install Boto3: pip install boto3
Configure AWS CLI: aws configure
- Provide your AWS credentials, region, and output format.

Script 1: Creating a CloudFormation Stack
File: 01-create-cloudformation-stack.py

import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation')

# Read the CloudFormation template file
with open('template.yaml', 'r') as template_file:
    template_body = template_file.read()

# Create the CloudFormation stack
try:
    response = cloudformation.create_stack(
        StackName='my-stack',
        TemplateBody=template_body,
        Parameters=[
            {'ParameterKey': 'InstanceType', 'ParameterValue': 't2.micro'}
        ],
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(f"CloudFormation stack created with ID: {response['StackId']}")
except Exception as e:
    print(f"Error creating CloudFormation stack: {e}")
Purpose:
This script creates a new CloudFormation stack using a template (template.yaml) and provisions resources like an EC2 instance.

Script 2: Viewing CloudFormation Stack Details
File: 02-view-cloudformation-stack.py

import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation')

# View stack details
try:
    response = cloudformation.describe_stacks(StackName='my-stack')
    stack = response['Stacks'][0]
    print(f"Stack Name: {stack['StackName']}")
    print(f"Stack Status: {stack['StackStatus']}")
    print(f"Creation Time: {stack['CreationTime']}")
    print(f"Outputs: {stack.get('Outputs', 'No Outputs')}")
except Exception as e:
    print(f"Error retrieving stack details: {e}")
Purpose:
This script retrieves and displays details of the specified CloudFormation stack, including its status and outputs.

Script 3: Deleting a CloudFormation Stack
File: 03-delete-cloudformation-stack.py

import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation')

# Delete the stack
try:
    cloudformation.delete_stack(StackName='my-stack')
    print("CloudFormation stack deletion initiated.")
except Exception as e:
    print(f"Error deleting stack: {e}")
Purpose:
This script deletes the specified CloudFormation stack and its associated resources.

Template File: template.yaml

AWSTemplateFormatVersion: '2010-09-09'
Description: 'AWS CloudFormation Template to create an EC2 instance with a security group.'

Parameters:
  InstanceType:
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.nano
      - t2.micro
      - t2.small
    Description: EC2 instance type

Resources:
  MyEC2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: 'ami-0c55b159cbfafe1f0'  # Example Amazon Linux 2 AMI in us-east-1
      SecurityGroups:
        - !Ref InstanceSecurityGroup

  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: 'Enable SSH access'
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0

Outputs:
  InstanceId:
    Description: 'Instance ID of the EC2 instance'
    Value: !Ref MyEC2Instance
  PublicIP:
    Description: 'Public IP address of the EC2 instance'
    Value: !GetAtt MyEC2Instance.PublicIp

Purpose:
Defines an EC2 instance and a security group for SSH access. Outputs the instance ID and public IP.

Instructions
Prepare the Environment:
Save the template.yaml file in the same directory as your scripts.
Run the Scripts:

Create the stack: python 01-create-cloudformation-stack.py
View stack details: python 02-view-cloudformation-stack.py
Delete the stack: python 03-delete-cloudformation-stack.py

Summary
AWS CloudFormation simplifies infrastructure management through automation and consistency. By using both the AWS Management Console and Boto3, you can efficiently create, manage, and delete resources. These tools are essential for DevOps, DevSecOps, and Python developers to implement Infrastructure as Code (IaC) practices.






