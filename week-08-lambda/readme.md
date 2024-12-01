AWS Lambda Functions with AWS GUI and Boto3
Objective
Learn how to create, configure, and invoke AWS Lambda functions using both the AWS Management Console and Boto3.

Part 1: Managing AWS Lambda Functions with the AWS GUI
Step 1: Creating an AWS Lambda Function
- Log in to the AWS Management Console:
- Visit AWS Management Console.
- Sign in using your AWS credentials.
- Navigate to Lambda:
- Search for "Lambda" in the services search bar and click on Lambda.
- Create a New Lambda Function:
- Click Create function.
- Choose "Author from scratch".
- Enter a function name (e.g., my_lambda_function).
- Select the Runtime (e.g., Python 3.8).
- Set the Permissions by selecting an existing role or creating a new role (e.g., AWSLambdaBasicExecutionRole).
- Click Create function.
Outcome: The Lambda function will be created and displayed in the console.

Step 2: Upload Code to the Lambda Function
Upload Lambda Code:

- On the function's configuration page, scroll to the Function code section.
- Under Code source, click Upload from, then select .zip file.
- Upload the lambda_function.zip file containing your lambda_function.py.
- Click Save.
Outcome: Your Lambda function code will be updated.

Step 3: Invoking the AWS Lambda Function
Test the Lambda Function:

- Click the Test button on the function's configuration page.
- Create a new test event:
- Name the event (e.g., testEvent).
- Use the following JSON input:

{
  "key": "value"
}

- Click Create.
- Click Test to execute the function.
Outcome: The Lambda function will execute, and the result will display in the console.

Part 2: Managing AWS Lambda Functions with Boto3
Prerequisites
- Install Boto3: pip install boto3
- Configure AWS CLI: aws configure
- Provide your Access Key, Secret Key, Region, and Output format.

Step 1: Creating an AWS Lambda Function with Boto3
- Create a file named 01_create_lambda.py:

import boto3
import json

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Read the zipped Lambda code
with open('lambda_function.zip', 'rb') as f:
    zipped_code = f.read()

# Create a new Lambda function
response = lambda_client.create_function(
    FunctionName='my_lambda_function',
    Runtime='python3.8',
    Role='arn:aws:iam::YOUR_ACCOUNT_ID:role/execution_role',  # Replace with your actual role ARN
    Handler='lambda_function.lambda_handler',  # Handler function in lambda_function.py
    Code=dict(ZipFile=zipped_code),
    Timeout=300,  # Execution time limit in seconds
    MemorySize=128  # Memory allocated to the function in MB
)

print("Lambda function created:", response['FunctionArn'])
Instructions:

- Create a Python file named lambda_function.py with the following content:

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }

- Zip the file:

zip lambda_function.zip lambda_function.py
Run the script to create the Lambda function:

python 01_create_lambda.py

Outcome: The Lambda function will be created using Boto3.

Step 2: Invoking the AWS Lambda Function with Boto3
- Create a file named 02_invoke_lambda.py:

import boto3
import json

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName='my_lambda_function',
    InvocationType='RequestResponse',
    Payload=json.dumps({'key': 'value'})
)

# Print the response from the Lambda function
print("Lambda function response:", response['Payload'].read().decode('utf-8'))
Instructions:

- Run the script to invoke the Lambda function:

python 02_invoke_lambda.py
Outcome: The script will invoke the Lambda function with a JSON payload and display the response.

Summary
Creating Lambda Functions:
- Used both the AWS Management Console and Boto3 to create a Lambda function.
- Uploaded the function code via .zip file.
- Invoking Lambda Functions:
- Tested the function through the AWS Console and invoked it programmatically with Boto3.
