import boto3
import botocore

# Initialize the S3 client with a specific region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

# Function to create a bucket
def create_bucket(bucket_name, region):
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
        print(f"Bucket '{bucket_name}' created successfully.")
    except botocore.exceptions.ClientError as e:
        print(f"Error creating bucket '{bucket_name}': {e}")

# Create the first bucket
create_bucket('alexboto-new-bucket-1', region)

# Create the second bucket
create_bucket('alexboto-new-bucket-2', region)

# Upload a file
local_file = 'local_file.txt'
bucket_name = 'alexboto-new-bucket-1'  # Ensure this matches the created bucket
s3_key = 'remote_file.txt'

try:
    s3.upload_file(local_file, bucket_name, s3_key)
    print(f"File '{local_file}' uploaded to bucket '{bucket_name}' with key '{s3_key}'.")
except botocore.exceptions.ClientError as e:
    print(f"Error uploading file '{local_file}' to bucket '{bucket_name}': {e}")
