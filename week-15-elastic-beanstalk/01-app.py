import boto3
import json

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

app_name = 'my-app'  # Replace with your desired application name

try:
    eb.create_application(ApplicationName=app_name)
    print(f"Application '{app_name}' created successfully.")
except eb.exceptions.TooManyApplicationsException:
    print(f"Application '{app_name}' already exists.")

# Save the application name to a JSON file
data = {'ApplicationName': app_name}
with open('beanstalk_app.json', 'w') as f:
    json.dump(data, f)
