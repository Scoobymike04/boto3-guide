import boto3
import json

# Load the Volume ID and Instance ID from the previously saved JSON file
with open('resource_ids.json', 'r') as f:
    data = json.load(f)
    volume_id = data['VolumeId']  # Get the Volume ID
    instance_id = data['InstanceId']  # Get the Instance ID

# Initialize EC2 client to interact with EC2 resources
ec2 = boto3.client('ec2')

# Define the device name for the EBS volume attachment
device = '/dev/sdf'  # Specify the device name where the volume will be attached

# Attach the EBS volume to the EC2 instance
response = ec2.attach_volume(
    VolumeId=volume_id,  # Attach the volume with this Volume ID
    InstanceId=instance_id,  # Attach to this EC2 instance
    Device=device  # Attach the volume as the specified device
)

print(f"Volume {volume_id} attached to instance {instance_id}")
