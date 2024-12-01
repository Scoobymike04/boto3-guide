import boto3
import json

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Step 1: Create EC2 Instance
response = ec2.run_instances(
    ImageId='ami-06b21ccaeff8cd686',  # Replace with your desired AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Use a free-tier eligible instance type
    KeyName='boto-test'  # Replace with your key pair name
)

# Extract instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance created with ID: {instance_id}")

# Save the instance ID to a JSON file for future tasks
data = {'InstanceId': instance_id}

with open('resource_ids.json', 'w') as f:
    json.dump(data, f)
