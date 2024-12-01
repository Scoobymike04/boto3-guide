import boto3
import json

# Load app and environment settings from JSON
with open('beanstalk_app.json', 'r') as f:
    data = json.load(f)
    app_name = data['ApplicationName']
    cname_prefix = data['CNAMEPrefix']
    solution_stack = data['SolutionStackName']

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

response = eb.create_environment(
    ApplicationName=app_name,
    EnvironmentName='my-env',  # Replace with your desired environment name
    SolutionStackName=solution_stack,
    CNAMEPrefix=cname_prefix
)

environment_id = response['EnvironmentId']
environment_name = response['EnvironmentName']
print(f"Environment created with ID: {environment_id} and CNAME prefix: {cname_prefix}")

# Save environment data to JSON
data.update({'EnvironmentId': environment_id, 'EnvironmentName': environment_name})
with open('beanstalk_env.json', 'w') as f:
    json.dump(data, f)
