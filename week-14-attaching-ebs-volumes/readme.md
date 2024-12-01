Creating and Attaching EBS Volumes with AWS GUI and Boto3

This guide demonstrates how to create, attach, view, and delete Elastic Block Store (EBS) volumes using both the AWS Management Console and the Boto3 Python library. These operations are essential for managing scalable and cost-efficient cloud storage solutions in AWS.

Part 1: Using the AWS Management Console
Steps to Create, Attach, and View EBS Volumes
- Log in to the AWS Management Console
- Navigate to the AWS Management Console and log in with your credentials.
- Navigate to the EC2 Dashboard
- Search for "EC2" in the services search bar and select it.

Create a New EBS Volume
- Under the "Elastic Block Store" section, click Volumes.
- Click Create Volume.
- Configure the following:
    Availability Zone: Ensure it matches the EC2 instance location (e.g., us-west-2a).
    Size: Specify the size in GiB (e.g., 10 GiB).
    Volume Type: Choose gp2 for general-purpose SSD or another type as needed.
    Encryption: Optionally enable encryption using AWS KMS.
- Click Create Volume.
Outcome: A new EBS volume is created.

Attach the Volume to an EC2 Instance
- Select the created volume and click Actions > Attach Volume.
- Select the instance from the dropdown.
- Specify the device name (e.g., /dev/sdf) and click Attach.
Outcome: The volume is attached to the EC2 instance.

View Attached Volumes
- Go to the Instances section, select the instance, and navigate to the Storage tab.
- Verify that the volume is listed with the specified device name.
Outcome: The attached volume is visible under the instance's details.

Delete the Volume
- Navigate to the Volumes section, select the volume, and click Actions > Delete Volume.
- Confirm the deletion.
Outcome: The volume is deleted and no longer incurs charges.

Part 2: Using Boto3
Prerequisites
Install Boto3: pip install boto3
Configure AWS CLI: aws configure
- Provide your AWS Access Key, Secret Key, Region, and Output format to allow Boto3 to interact with AWS services.

Step-by-Step Scripts
1. Create an EC2 Instance and Store IDs

import boto3
import json

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Create an EC2 instance
response = ec2.run_instances(
    ImageId='ami-06b21ccaeff8cd686',  # Replace with your desired AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Free-tier eligible instance type
    KeyName='your-key-pair-name'  # Replace with your key pair
)

instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance created with ID: {instance_id}")

# Save Instance ID to a JSON file
data = {'InstanceId': instance_id}
with open('resource_ids.json', 'w') as file:
    json.dump(data, file)

2. Create an EBS Volume

import boto3
import json

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Create a new EBS volume
response = ec2.create_volume(
    AvailabilityZone='us-west-2a',  # Match the instance's AZ
    Size=10,  # Size in GiB
    VolumeType='gp2'  # General-purpose SSD
)

volume_id = response['VolumeId']
print(f"Volume created with ID: {volume_id}")

# Load instance ID and update JSON file with Volume ID
with open('resource_ids.json', 'r') as file:
    data = json.load(file)
data['VolumeId'] = volume_id
with open('resource_ids.json', 'w') as file:
    json.dump(data, file)

3. Attach the EBS Volume

import boto3
import json

# Load Instance ID and Volume ID
with open('resource_ids.json', 'r') as file:
    data = json.load(file)

instance_id = data['InstanceId']
volume_id = data['VolumeId']

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Attach the volume
device_name = '/dev/sdf'  # Specify the device name
response = ec2.attach_volume(
    VolumeId=volume_id,
    InstanceId=instance_id,
    Device=device_name
)

print(f"Volume {volume_id} attached to instance {instance_id} as {device_name}")

4. View Attached Volumes

import boto3
import json

# Load Instance ID
with open('resource_ids.json', 'r') as file:
    data = json.load(file)

instance_id = data['InstanceId']

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Describe the instance
response = ec2.describe_instances(InstanceIds=[instance_id])

# List attached volumes
volumes = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings']
for volume in volumes:
    print(f"Volume ID: {volume['Ebs']['VolumeId']} attached as {volume['DeviceName']}")

5. Detach and Delete the Volume

import boto3
import json
import time

# Load Volume ID
with open('resource_ids.json', 'r') as file:
    data = json.load(file)
volume_id = data['VolumeId']

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Detach the volume
response = ec2.detach_volume(VolumeId=volume_id, Force=True)
print(f"Detaching volume {volume_id}...")

# Wait until the volume is detached
while True:
    volume_info = ec2.describe_volumes(VolumeIds=[volume_id])
    state = volume_info['Volumes'][0]['State']
    if state == 'available':
        print(f"Volume {volume_id} is now detached.")
        break
    time.sleep(5)

# Delete the volume
response = ec2.delete_volume(VolumeId=volume_id)
print(f"Volume {volume_id} deleted.")

Use Cases and Benefits
For Python Developers
- Automated Storage Management: Create, attach, and delete volumes programmatically for temporary or scalable storage.
- Disaster Recovery: Automate backups using snapshots to ensure data safety.
For DevOps/DevSecOps Engineers
- Infrastructure as Code (IaC): Use Boto3 to integrate EBS volume management into automated deployment pipelines.
- Cost Optimization: Automate volume cleanup to avoid unnecessary charges for unused resources.

Costs
EBS Volume Pricing:
- General Purpose SSD (gp2): $0.10 per GiB per month.
- Provisioned IOPS SSD (io1): $0.125 per GiB per month, plus $0.065 per provisioned IOPS per month.
Snapshots:
- $0.05 per GiB-month for stored snapshots.
Data Transfer:
- Free within the same Availability Zone. Cross-region or inter-service transfers may incur charges.

Conclusion
By automating EBS volume management with Boto3, you can achieve scalable, reliable, and cost-efficient storage for your cloud applications. These scripts simplify dynamic resource provisioning and ensure that storage solutions align with application requirements. Whether for development, testing, or production, these workflows enhance cloud management and productivity.






