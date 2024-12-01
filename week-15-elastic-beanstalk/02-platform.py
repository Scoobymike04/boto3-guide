import boto3
import json
import uuid

# Load application details from JSON
with open('beanstalk_app.json', 'r') as f:
    data = json.load(f)
    app_name = data['ApplicationName']

# Initialize the Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

# Generate a unique CNAME prefix using UUID
cname_prefix = f"{app_name}-{uuid.uuid4().hex[:8]}"
solution_stack = '64bit Amazon Linux 2023 v4.2.0 running Python 3.9'  # Update if needed

# Save the CNAME and platform to JSON
data.update({'CNAMEPrefix': cname_prefix, 'SolutionStackName': solution_stack})
with open('beanstalk_app.json', 'w') as f:
    json.dump(data, f)

print(f"CNAME prefix set to: {cname_prefix}")
print(f"Platform set to: {solution_stack}")
