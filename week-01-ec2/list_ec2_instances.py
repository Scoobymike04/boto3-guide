import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_ec2_instances():
    try:
        # Initialize a session using Amazon EC2
        session = boto3.Session(region_name='us-east-1')  # Specify your region here
        ec2 = session.resource('ec2')

        # List all instances
        for instance in ec2.instances.all():
            print("Instance ID: ", instance.id)
            print("Instance State: ", instance.state['Name'])
            print("Instance Type: ", instance.instance_type)
            print("Public IP Address: ", instance.public_ip_address)
            print("Private IP Address: ", instance.private_ip_address)
            print("----" * 10)
    except NoCredentialsError:
        print("Credentials not available. Please check your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete credentials provided. Please check your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_ec2_instances()
