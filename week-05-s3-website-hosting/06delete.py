import boto3
import botocore

# Initialize the S3 client with the correct region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

bucket_name = 'alex-devops-bucket'  # Replace with your bucket name

# Delete the objects in the bucket
try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        print(f"All objects deleted from bucket '{bucket_name}'.")
    else:
        print(f"No objects to delete in bucket '{bucket_name}'.")
except botocore.exceptions.ClientError as e:
    print(f"Error listing or deleting objects in bucket '{bucket_name}': {e}")

# Delete the bucket
try:
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
except botocore.exceptions.ClientError as e:
    print(f"Error deleting bucket '{bucket_name}': {e}")
