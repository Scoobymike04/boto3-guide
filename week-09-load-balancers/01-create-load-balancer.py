import boto3

# Initialize the ELBv2 client
elb = boto3.client('elbv2')

# Create a new load balancer with at least two subnets in different Availability Zones
response = elb.create_load_balancer(
    Name='my-load-balancer',
    Subnets=[
        'subnet-056fbe0fd2554c943',  # Replace with actual Subnet ID in AZ1
        'subnet-0d2e0e923b9b39b0c'   # Replace with actual Subnet ID in AZ2
    ],
    SecurityGroups=['sg-0d575bbe51ff5c2ed'],  # Replace with actual security group IDs - this is using the default VPC in us-east-1
    Scheme='internet-facing',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-load-balancer'
        }
    ],
    Type='application',
    IpAddressType='ipv4'
)

# Output the ARN of the created load balancer
load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load balancer created with ARN: {load_balancer_arn}")
