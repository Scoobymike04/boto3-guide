import boto3
import json

# Load the application and environment details from JSON
try:
    with open('beanstalk_app.json', 'r') as f:
        data = json.load(f)
        app_name = data.get('ApplicationName')
        cname_prefix = data.get('CNAMEPrefix')
        solution_stack = data.get('SolutionStackName')
except FileNotFoundError:
    print("Configuration file 'beanstalk_app.json' not found. Please ensure the application details are saved correctly.")
    exit()

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

# Check if the environment already exists
try:
    response = eb.describe_environments(ApplicationName=app_name)
    existing_environments = {env['EnvironmentName']: env['Status'] for env in response['Environments']}

    if 'my-env' in existing_environments:
        print(f"Environment 'my-env' already exists with status: {existing_environments['my-env']}")
    else:
        # Recreate the environment if it does not exist
        response = eb.create_environment(
            ApplicationName=app_name,
            EnvironmentName='my-env',  # Recreate the original environment name
            SolutionStackName=solution_stack,
            CNAMEPrefix=cname_prefix
        )
        environment_id = response['EnvironmentId']
        print(f"Elastic Beanstalk environment restored with ID: {environment_id} and CNAME prefix: {cname_prefix}")
        
        # Save the new environment ID to JSON
        data['EnvironmentId'] = environment_id
        data['EnvironmentName'] = 'my-env'
        with open('beanstalk_env.json', 'w') as f:
            json.dump(data, f)
except Exception as e:
    print(f"An error occurred while restoring the environment: {e}")
