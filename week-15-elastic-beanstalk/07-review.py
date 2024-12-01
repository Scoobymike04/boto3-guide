import boto3
import json

# Load the application and environment details from JSON
try:
    with open('beanstalk_env.json', 'r') as f:
        data = json.load(f)
        app_name = data.get('ApplicationName')
        environment_name = data.get('EnvironmentName')
except FileNotFoundError:
    print("Configuration file 'beanstalk_env.json' not found. Ensure it contains the application and environment details.")
    exit()

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

# Describe the application
try:
    app_response = eb.describe_applications(ApplicationNames=[app_name])
    if app_response['Applications']:
        application = app_response['Applications'][0]
        print(f"Application Name: {application['ApplicationName']}")
        print(f"Description: {application.get('Description', 'N/A')}")
        print(f"Date Created: {application['DateCreated']}")
        print(f"Date Updated: {application['DateUpdated']}")
    else:
        print(f"No application found with name '{app_name}'.")

    # Describe the environment
    env_response = eb.describe_environments(
        ApplicationName=app_name,
        EnvironmentNames=[environment_name]
    )

    if env_response['Environments']:
        environment = env_response['Environments'][0]
        print(f"\nEnvironment Name: {environment['EnvironmentName']}")
        print(f"Environment Status: {environment['Status']}")
        print(f"Environment Health: {environment['Health']}")
        print(f"Environment URL: {environment['CNAME']}")
    else:
        print(f"No environment found with name '{environment_name}'.")

except Exception as e:
    print(f"An error occurred while retrieving details: {e}")
