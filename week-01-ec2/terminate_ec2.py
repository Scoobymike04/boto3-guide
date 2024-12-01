import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def terminate_ec2_instance(instance_id):
    try:
        # Initialize a session using Amazon EC2
        session = boto3.Session(region_name='us-east-1')  # Specify your region here
        ec2 = session.resource('ec2')

        # Terminate the EC2 instance
        ec2.instances.filter(InstanceIds=[instance_id]).terminate()
        print(f"Instance terminated: {instance_id}")
    except NoCredentialsError:
        print("Credentials not available. Please check your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete credentials provided. Please check your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Instance ID to terminate (replace with your actual instance ID)
    instance_id = 'i-0813b979fbffa3a6f'  # Replace with your instance ID
    terminate_ec2_instance(instance_id)
