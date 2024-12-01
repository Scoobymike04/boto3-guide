Automating Static Website Hosting with S3 and Python

This lesson provides a step-by-step guide to:

Download a video from YouTube.
Create and configure an S3 bucket to host a static website.
Upload the video and an HTML file to the S3 bucket.
Retrieve the bucket name and public URL.
Send the bucket information to your email.
Steps

1. Download a Video from YouTube
Use yt-dlp to download videos from YouTube. This tool is actively maintained and reliable for handling changes in YouTube’s platform.

Instructions:
Install yt-dlp:

pip install yt-dlp
Create a Python script to download the video:

File: 01download.py

import sys
from yt_dlp import YoutubeDL

if len(sys.argv) != 2:
    print("Usage: python 01download.py <URL>")
    sys.exit(1)

video_url = sys.argv[1]
save_path = 'video.mp4'

try:
    ydl_opts = {'outtmpl': save_path}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f'Video downloaded successfully and saved as {save_path}')
except Exception as e:
    print(f"Error downloading video: {e}")
Run the script:

python 01download.py "https://www.youtube.com/watch?v=example"

2. Create and Configure an S3 Bucket
Host the video as part of a static website on AWS S3.

Instructions:
Create an S3 bucket and configure it:

File: 02create.py

import boto3
import botocore
import json

region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)
bucket_name = 'my-static-website-bucket'

try:
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    print(f"Bucket '{bucket_name}' created successfully.")
except botocore.exceptions.ClientError as e:
    print(f"Error creating bucket '{bucket_name}': {e}")

website_configuration = {
    'IndexDocument': {'Suffix': 'index.html'},
    'ErrorDocument': {'Key': 'error.html'}
}

try:
    s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)
    print(f"Bucket '{bucket_name}' configured as a static website.")
except botocore.exceptions.ClientError as e:
    print(f"Error configuring bucket '{bucket_name}' as a static website: {e}")

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

3. Upload the Video and index.html to the S3 Bucket
Add the downloaded video and an HTML file to the S3 bucket.

Instructions:
Create an HTML file (index.html) for the static website.

Upload the files to the bucket using AWS CLI or Boto3.

File: 03upload.py

import boto3

s3 = boto3.client('s3')
bucket_name = 'my-static-website-bucket'

try:
    s3.upload_file('video.mp4', bucket_name, 'video.mp4')
    print("Video uploaded successfully.")
    s3.upload_file('index.html', bucket_name, 'index.html')
    print("index.html uploaded successfully.")
except Exception as e:
    print(f"Error uploading files: {e}")
Run the script:

python 03upload.py

4. Print the Bucket Name and Public URL
Retrieve the bucket information.

Instructions:
File: print_bucket_info.py

bucket_name = 'my-static-website-bucket'
region = 'us-east-1'
public_url = f'http://{bucket_name}.s3-website-{region}.amazonaws.com'

print(f"Bucket Name: {bucket_name}")
print(f"Public URL: {public_url}")

5. Send the Bucket Information to Your Email
Use AWS SES to send the bucket name and public URL to your email.

Instructions:
Set up AWS SES and verify your email.

Create a Python script to send an email.

File: send_email.py

import boto3

region = 'us-east-1'
ses = boto3.client('ses', region_name=region)
bucket_name = 'my-static-website-bucket'
public_url = f'http://{bucket_name}.s3-website-{region}.amazonaws.com'

sender_email = 'your-email@example.com'
recipient_email = 'your-email@example.com'
subject = 'S3 Static Website Information'
body_text = (f"Bucket Name: {bucket_name}\n"
             f"Public URL: {public_url}")

try:
    ses.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body_text}}
        }
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
Run the script:

python send_email.py
Summary of Steps
- Download a video from YouTube using yt-dlp and save it locally.
- Create an S3 bucket and configure it for static website hosting.
- Upload the video and index.html to the S3 bucket.
- Retrieve and print the bucket name and public URL.
- Send the bucket information to your email using AWS SES.
