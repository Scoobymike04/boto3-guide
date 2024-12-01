import boto3

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

# List available solution stacks
response = eb.list_available_solution_stacks()

# Print all solution stacks
print("Available Solution Stacks:")
for stack in response['SolutionStacks']:
    print(stack)
