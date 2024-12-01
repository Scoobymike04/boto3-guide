import boto3
import json
import time

# Load the Volume ID and Instance ID from the saved JSON file
with open('resource_ids.json', 'r') as f:
    data = json.load(f)
    volume_id = data['VolumeId']  # Get the Volume ID
    instance_id = data['InstanceId']  # Get the Instance ID

# Initialize EC2 client to interact with EC2 resources
ec2 = boto3.client('ec2')

# Step 1: Detach the EBS volume if it's attached
try:
    # Describe the volume to check its state
    volume_info = ec2.describe_volumes(VolumeIds=[volume_id])
    
    # Check if the volume is attached to an instance
    if volume_info['Volumes'][0]['State'] == 'in-use':
        print(f"Volume {volume_id} is currently attached. Detaching the volume...")
        
        # Detach the volume
        ec2.detach_volume(VolumeId=volume_id, Force=True)
        
        # Wait until the volume is fully detached
        while True:
            volume_info = ec2.describe_volumes(VolumeIds=[volume_id])
            volume_state = volume_info['Volumes'][0]['State']
            if volume_state == 'available':
                print(f"Volume {volume_id} successfully detached and is now available for deletion.")
                break
            else:
                print(f"Waiting for volume to detach...")
            time.sleep(5)  # Wait 5 seconds before checking again
    else:
        print(f"Volume {volume_id} is not in use and can be deleted.")

except Exception as e:
    print(f"An error occurred while detaching the volume: {e}")

# Step 2: Delete the EBS volume
try:
    response = ec2.delete_volume(VolumeId=volume_id)
    print(f"Volume {volume_id} deleted successfully.")
except Exception as e:
    print(f"An error occurred while deleting the volume: {e}")

# Step 3: Terminate the EC2 instance
try:
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} has been terminated.")
except Exception as e:
    print(f"An error occurred while terminating the instance: {e}")
