import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation')

# Read the CloudFormation template file
with open('template.yaml', 'r') as template_file:
    template_body = template_file.read()

# Create the CloudFormation stack
try:
    response = cloudformation.create_stack(
        StackName='my-stack',
        TemplateBody=template_body,
        Parameters=[
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            }
        ],
        Capabilities=[
            'CAPABILITY_NAMED_IAM'
        ]
    )
    print(f"CloudFormation stack created with ID: {response['StackId']}")
except Exception as e:
    print(f"Error creating CloudFormation stack: {e}")
