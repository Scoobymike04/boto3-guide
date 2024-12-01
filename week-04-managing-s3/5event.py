import boto3

# Initialize the S3 client with the correct region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

# Define the bucket name and Lambda function ARN
bucket_name = 'alexboto-new-bucket-1'
lambda_function_arn = 'arn:aws:lambda:us-east-1:891376916144:function:S3EventProcessor'

# Define the notification configuration
notification_configuration = {
    'LambdaFunctionConfigurations': [
        {
            'LambdaFunctionArn': lambda_function_arn,
            'Events': ['s3:ObjectCreated:*']
        }
    ]
}

try:
    # Set up the bucket notification configuration
    s3.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration=notification_configuration
    )
    print(f"S3 event notification for Lambda function '{lambda_function_arn}' set up successfully.")
except Exception as e:
    print(f"Error setting up S3 event notification: {e}")
