import boto3
import botocore

# Initialize the S3 client with the correct region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

# Define the bucket names
source_bucket_name = 'alexboto-new-bucket-1'
target_bucket_name = 'alexboto-new-bucket-2'

# Function to delete all objects in a bucket
def delete_all_objects(bucket_name):
    try:
        # List objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"All objects in bucket '{bucket_name}' deleted successfully.")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")
    except botocore.exceptions.ClientError as e:
        print(f"Error deleting objects in bucket '{bucket_name}': {e}")

# Function to remove bucket notification configuration
def remove_bucket_notification(bucket_name):
    try:
        s3.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration={}
        )
        print(f"Bucket notification configuration for '{bucket_name}' removed successfully.")
    except botocore.exceptions.ClientError as e:
        print(f"Error removing bucket notification configuration for '{bucket_name}': {e}")

# Function to disable bucket logging configuration
def disable_bucket_logging(source_bucket_name):
    try:
        s3.put_bucket_logging(
            Bucket=source_bucket_name,
            BucketLoggingStatus={}
        )
        print(f"Logging configuration for bucket '{source_bucket_name}' disabled successfully.")
    except botocore.exceptions.ClientError as e:
        print(f"Error disabling logging configuration for bucket '{source_bucket_name}': {e}")

# Function to delete a bucket
def delete_bucket(bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except botocore.exceptions.ClientError as e:
        print(f"Error deleting bucket '{bucket_name}': {e}")

# Delete all objects in the source and target buckets
delete_all_objects(source_bucket_name)
delete_all_objects(target_bucket_name)

# Remove bucket notification configuration from the source bucket
remove_bucket_notification(source_bucket_name)

# Disable logging configuration for the source bucket
disable_bucket_logging(source_bucket_name)

# Delete the source and target buckets
delete_bucket(source_bucket_name)
delete_bucket(target_bucket_name)

print("All files, events, logs, and buckets have been deleted successfully.")