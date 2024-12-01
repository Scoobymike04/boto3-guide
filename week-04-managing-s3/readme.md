Managing S3 Buckets with AWS GUI and Boto3
Objective
Learn how to create, delete, upload, and download files in S3 buckets using both the AWS Management Console and Boto3. Additionally, learn to configure event notifications, logging, and automation with Lambda for efficient resource management.

Part 1: Managing S3 Buckets Using the AWS Management Console
Creating an S3 Bucket
- Log in to the AWS Management Console.
- Search for "S3" and select the service.
- Click "Create bucket."
- Enter a unique bucket name and select a region.
- Configure additional settings (e.g., block public access, versioning, encryption).
- Click "Create bucket."
Deleting an S3 Bucket
- Navigate to the S3 service.
- Find and select the bucket to delete.
- Click "Delete bucket."
- Confirm the deletion by typing the bucket name.
Uploading a File to S3
- Navigate to the desired bucket in the S3 service.
- Click "Upload."
- Add the file(s) and click "Upload."
Downloading a File from S3
- Navigate to the bucket containing the file.
- Select the file and click "Download."
Setting Up S3 Event Notification
- Go to the bucket's "Properties" tab.
- Under "Event notifications," click "Create event notification."
- Specify an event type (e.g., "All object create events").
- Link the notification to a Lambda function.
- Save the configuration.
Configuring Bucket Logging
- Navigate to the bucket's "Properties" tab.
- Under "Server access logging," click "Edit."
- Specify a target bucket for logs and a prefix (optional).
- Save the configuration.
Copying an Object Between Buckets
- Navigate to the source bucket and locate the object.
- Select "Actions" > "Copy."
- Choose the destination bucket and specify the key.
- Confirm the operation.

Part 2: Managing S3 Buckets Using Boto3
Prerequisites
- Install Boto3: pip install boto3.
- Configure AWS CLI: aws configure.

Creating an S3 Bucket

import boto3
s3 = boto3.client('s3')
bucket_name = 'my-new-bucket'
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' created.")

Deleting an S3 Bucket

bucket_name = 'my-new-bucket'
s3.delete_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' deleted.")

Uploading a File

s3.upload_file('local_file.txt', 'my-new-bucket', 'uploaded_file.txt')
print("File uploaded successfully.")

Downloading a File

s3.download_file('my-new-bucket', 'uploaded_file.txt', 'local_copy.txt')
print("File downloaded successfully.")

Setting Up S3 Event Notifications

notification_config = {
    'LambdaFunctionConfigurations': [
        {
            'LambdaFunctionArn': 'arn:aws:lambda:region:account-id:function:MyFunction',
            'Events': ['s3:ObjectCreated:*']
        }
    ]
}
s3.put_bucket_notification_configuration(
    Bucket='my-new-bucket',
    NotificationConfiguration=notification_config
)
print("Event notification configured.")
Configuring Bucket Logging

logging_config = {
    'LoggingEnabled': {
        'TargetBucket': 'log-target-bucket',
        'TargetPrefix': 'logs/'
    }
}
s3.put_bucket_logging(
    Bucket='my-new-bucket',
    BucketLoggingStatus=logging_config
)
print("Bucket logging configured.")

Copying an Object Between Buckets

copy_source = {'Bucket': 'source-bucket', 'Key': 'source-key'}
s3.copy_object(CopySource=copy_source, Bucket='target-bucket', Key='target-key')
print("Object copied successfully.")

Automating S3 Processes with AWS Lambda

Why Automate with Lambda?
- Efficiency: Reduces manual intervention.
- Scalability: Handles large volumes of data seamlessly.
- Cost-Effectiveness: Optimizes resource utilization.
- Error Reduction: Ensures consistent and reliable operations.

Common Use Cases
- File Processing: Transform or validate files upon upload.
- Alerts and Monitoring: Notify on specific events.
- Cleanup: Automate deletion of old or unnecessary files.

Example: Real-Time Data Validation

Scenario
Validate files uploaded to an S3 bucket. If errors are detected, move files to an error bucket and delete the original.

Lambda Function Code
import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        
        if "error" in content:
            error_bucket = 'error-bucket'
            s3.copy_object(
                Bucket=error_bucket, 
                CopySource={'Bucket': bucket, 'Key': key}, 
                Key=key
            )
            s3.delete_object(Bucket=bucket, Key=key)
            print(f"File {key} moved to {error_bucket}")
        
        return {"statusCode": 200, "body": "File processed successfully"}
    except Exception as e:
        print(f"Error processing file {key}: {e}")
        raise e
Summary
In this lesson, you learned how to manage S3 buckets using both the AWS Management Console and Boto3, configure event-driven processes with Lambda, and implement logging and automation for efficient resource management. These skills enhance your ability to handle cloud storage tasks, automate workflows, and optimize AWS operations.







