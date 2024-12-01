AWS EC2 and Boto3 Guide
What is AWS EC2?
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers by offering scalable infrastructure on demand.
________________________________________
Why was AWS EC2 Developed?
1.	Scalability: Easily scale up or down based on demand, providing the exact compute power needed at any given time.
2.	Flexibility: A wide variety of instance types tailored to different use cases.
3.	Cost-Effectiveness: Pay only for the compute power you use, with various pricing models to save costs.
4.	Reliability: High availability and robust infrastructure designed to minimize downtime.
________________________________________
Importance for DevSecOps and Python Developers
For DevSecOps:
•	Automation: Streamline infrastructure provisioning and management with tools.
•	Scalability: Ensure high availability and performance with dynamic scaling.
•	Security: Enforce policies and access controls.
•	Monitoring: Track performance and availability proactively.
For Python Developers:
•	Development and Testing: Quickly provision development environments.
•	Automation: Leverage Python scripts and libraries like Boto3 for task automation.
•	Integration: Build applications that interact with AWS services such as S3, RDS, and Lambda.
•	Resource Management: Optimize performance and cost.
________________________________________
Why Use Boto3 for EC2 Management?
Boto3 is the AWS SDK for Python, enabling programmatic interaction with AWS services.
Benefits:
1.	Programmatic Access: Automate EC2 tasks, reducing errors and increasing efficiency.
2.	CI/CD Integration: Manage EC2 resources as part of CI/CD pipelines.
3.	Dynamic Resource Management: Adjust resources on demand.
4.	Automation: Simplify scaling, deployment, and monitoring.
________________________________________
Creating and Managing AWS Resources with EC2
Objective
By the end of this lesson, you will:
1.	Create and terminate EC2 instances using the AWS Management Console.
2.	Automate instance management using Python and Boto3.
________________________________________
Part 1: Using the AWS Management Console
Step 1: Creating an EC2 Instance
1.	Log in to AWS: 
o	Go to AWS Management Console.
2.	Navigate to EC2 Dashboard: 
o	In the Services menu, search for and select EC2.
3.	Launch an Instance: 
o	Click Launch Instance.
o	Select an Amazon Machine Image (AMI) (e.g., Amazon Linux 2 AMI).
o	Choose an Instance Type (e.g., t2.micro for the free tier).
o	Configure Instance Details (default settings are sufficient for this lesson).
o	Add Storage (default settings are sufficient).
o	Optionally, add a Tag (e.g., Key: Name, Value: MyEC2Instance).
o	Configure a Security Group: 
	Create a new security group and allow SSH (port 22).
o	Click Review and Launch.
o	Select an existing key pair or create a new one for SSH access. Confirm key pair access and launch the instance.
4.	View the Instance: 
o	Click View Instances to check the status of your new instance.
o	Wait for the instance state to become running.
________________________________________
Step 2: Terminating an EC2 Instance
1.	Go to the EC2 Dashboard: 
o	In the Services menu, search for EC2 and click it.
2.	Terminate the Instance: 
o	Select the instance to terminate.
o	Click Actions > Instance State > Terminate.
o	Confirm termination.
________________________________________
Part 2: Automating with Boto3 in Python
Prerequisites
1.	Install Boto3: pip install boto3
2.	Configure AWS CLI: aws configure
o	Provide your AWS Access Key, Secret Key, region, and output format.
________________________________________
Step 1: Creating an EC2 Instance with Boto3
Create a Python script to automate instance creation.
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_ec2_instance():
    try:
        # Initialize EC2 resource
        ec2 = boto3.resource('ec2')

        # Create a new EC2 instance
        instance = ec2.create_instances(
            ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro'
        )[0]

        print(f"Instance created: {instance.id}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        print("AWS credentials not found or incomplete:", e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_ec2_instance()
________________________________________
Step 2: Viewing EC2 Instances
List all running EC2 instances.
def list_ec2_instances():
    try:
        ec2 = boto3.resource('ec2')

        # List all instances
        for instance in ec2.instances.all():
            print(f"ID: {instance.id}, State: {instance.state['Name']}, Type: {instance.instance_type}")
    except Exception as e:
        print(f"Error listing instances: {e}")

if __name__ == "__main__":
    list_ec2_instances()
________________________________________
Step 3: Terminating an EC2 Instance
Terminate a specific instance.
def terminate_ec2_instance(instance_id):
    try:
        ec2 = boto3.resource('ec2')

        # Terminate instance
        instance = ec2.Instance(instance_id)
        instance.terminate()

        print(f"Instance terminated: {instance_id}")
    except Exception as e:
        print(f"Error terminating instance: {e}")

if __name__ == "__main__":
    terminate_ec2_instance("i-0abcdef1234567890")  # Replace with your instance ID
________________________________________
Common Errors and Solutions
1.	NoCredentialsError: 
o	Ensure credentials are configured using aws configure.
2.	Invalid AMI ID: 
o	Use a valid AMI ID for your region.
3.	Permissions Issue: 
o	Ensure your IAM user has the necessary permissions (e.g., ec2:RunInstances, ec2:TerminateInstances).
________________________________________
Conclusion
AWS EC2 provides scalable, flexible compute resources for developers. By combining manual instance management in the AWS Management Console with Boto3 automation, developers can efficiently manage their infrastructure and focus on building robust applications.
________________________________________
Example Output
Creating an Instance:
Instance created: i-0abcdef1234567890
Listing Instances:
ID: i-0abcdef1234567890, State: running, Type: t2.micro
Terminating an Instance:
Instance terminated: i-0abcdef1234567890

