import json
import boto3
import botocore
import time

# Initialize the S3 client with the correct region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

bucket_name = 'alex-devops-bucket'  # Replace with a unique bucket name

# Create the bucket
try:
    if region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    print(f"Bucket '{bucket_name}' created successfully.")
except botocore.exceptions.ClientError as e:
    print(f"Error creating bucket '{bucket_name}': {e}")

# Add a delay to ensure the bucket is fully created before continuing
time.sleep(5)

# Configure the bucket as a static website
website_configuration = {
    'IndexDocument': {'Suffix': 'index.html'},
    'ErrorDocument': {'Key': 'error.html'}
}

try:
    s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)
    print(f"Bucket '{bucket_name}' configured as a static website.")
except botocore.exceptions.ClientError as e:
    print(f"Error configuring bucket '{bucket_name}' as a static website: {e}")

# Set the bucket policy to make it public
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

try:
    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))
    print(f"Bucket policy set to make '{bucket_name}' public.")
except botocore.exceptions.ClientError as e:
    print(f"Error setting bucket policy for '{bucket_name}': {e}")

# Disable public access block settings for the bucket
bucket_public_access_block = {
    'BlockPublicAcls': False,
    'IgnorePublicAcls': False,
    'BlockPublicPolicy': False,
    'RestrictPublicBuckets': False
}

try:
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration=bucket_public_access_block
    )
    print(f"Public access block settings configured for '{bucket_name}'.")
except botocore.exceptions.ClientError as e:
    print(f"Error configuring public access block settings for '{bucket_name}': {e}")
