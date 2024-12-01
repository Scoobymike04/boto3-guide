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

# Upload files and set ACLs
def upload_file(file_name, bucket, object_name, content_type):
    try:
        s3.upload_file(
            file_name, bucket, object_name,
            ExtraArgs={'ContentType': content_type, 'ACL': 'public-read'}
        )
        print(f"File '{file_name}' uploaded to bucket '{bucket}' with key '{object_name}'.")
    except botocore.exceptions.ClientError as e:
        print(f"Error uploading file '{file_name}' to bucket '{bucket}': {e}")

# Create index.html and error.html files
index_html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My First Webpage</title>
</head>
<body>
    <h1>My First Webpage</h1>
    <video width="320" height="240" controls>
        <source src="https://{bucket_name}.s3.amazonaws.com/video.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>
"""

error_html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>Page not found</h1>
</body>
</html>
"""

with open('index.html', 'w') as file:
    file.write(index_html_content)

with open('error.html', 'w') as file:
    file.write(error_html_content)

# Upload index.html and error.html
upload_file('index.html', bucket_name, 'index.html', 'text/html')
upload_file('error.html', bucket_name, 'error.html', 'text/html')

# Upload the video file
upload_file('video.mp4', bucket_name, 'video.mp4', 'video/mp4')

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

# Print the URL of the website
website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
print(f"Website URL: {website_url}")
