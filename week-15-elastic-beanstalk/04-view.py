import boto3
import json

# Load environment details from JSON
with open('beanstalk_env.json', 'r') as f:
    data = json.load(f)
    app_name = data['ApplicationName']
    environment_name = data['EnvironmentName']

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

response = eb.describe_environments(
    ApplicationName=app_name,
    EnvironmentNames=[environment_name]
)

environment_details = response['Environments'][0]
print(f"Environment Name: {environment_details['EnvironmentName']}")
print(f"Environment Status: {environment_details['Status']}")
print(f"Environment Health: {environment_details['Health']}")
print(f"Environment URL: {environment_details['CNAME']}")
