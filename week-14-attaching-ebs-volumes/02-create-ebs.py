import boto3
import json

# Initialize EC2 client to communicate with EC2 resources
ec2 = boto3.client('ec2')

# Create a new EBS volume in a specified availability zone
response = ec2.create_volume(
    AvailabilityZone='us-east-1a',  # Specify the AZ where the volume will be created
    Size=10,  # Specify the size of the volume in GiB
    VolumeType='gp2'  # Specify the volume type (General Purpose SSD)
)

# Extract the Volume ID from the response
volume_id = response['VolumeId']
print(f"Volume created with ID: {volume_id}")

# Load the Instance ID from the previously saved JSON file
with open('resource_ids.json', 'r') as f:
    data = json.load(f)

# Save the updated Volume ID to the JSON file
data['VolumeId'] = volume_id

with open('resource_ids.json', 'w') as f:
    json.dump(data, f)
