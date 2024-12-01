import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Describe instances
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['InstanceType'], instance['State']['Name'])
