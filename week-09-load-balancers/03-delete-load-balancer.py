import boto3

# Initialize the ELBv2 client
elb = boto3.client('elbv2')

try:
    # Retrieve all load balancers
    response = elb.describe_load_balancers()

    # Check if there are any load balancers
    if len(response['LoadBalancers']) == 0:
        print("No load balancers found.")
    else:
        # Get the first load balancer's ARN
        load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']
        print(f"Load balancer ARN: {load_balancer_arn}")

        # Delete the load balancer using the retrieved ARN
        elb.delete_load_balancer(LoadBalancerArn=load_balancer_arn)
        print(f"Load balancer '{load_balancer_arn}' deleted successfully.")

except Exception as e:
    print(f"Error deleting load balancer: {e}")
