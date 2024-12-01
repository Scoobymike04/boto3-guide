import boto3
import json

# Load the Instance ID from the saved JSON file
with open('resource_ids.json', 'r') as f:
    data = json.load(f)
    instance_id = data['InstanceId']  # Get the Instance ID

# Initialize EC2 client to interact with EC2 resources
ec2 = boto3.client('ec2')

# Describe the EC2 instance to get information about attached volumes
response = ec2.describe_instances(InstanceIds=[instance_id])

# Extract information about attached volumes from the response
volumes = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings']
for volume in volumes:
    # Print the Volume ID and the device name for each attached volume
    print(f"Volume ID: {volume['Ebs']['VolumeId']} is attached to device {volume['DeviceName']}")
