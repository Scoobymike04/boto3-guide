import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Stop an instance
ec2.stop_instances(InstanceIds=['i-06c631f5640bfc2a2','i-0b3a70eaebf11c7d1','i-025095cf9022f12a9'])
print("Instance(s) stopped.")
