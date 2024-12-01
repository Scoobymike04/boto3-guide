import boto3 # type: ignore
from botocore.exceptions import NoCredentialsError, PartialCredentialsError # type: ignore

def create_ec2_instance():
    try:
        # Initialize a session using Amazon EC2
        ec2 = boto3.resource('ec2')
        
        # Create a new EC2 instance
        instances = ec2.create_instances(
            ImageId='ami-0195204d5dce06d99',  # Replace with a valid AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro'
        )
        print("New instance created: ", instances[0].id)
    except NoCredentialsError:
        print("Credentials not available. Please check your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete credentials provided. Please check your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_ec2_instance()
