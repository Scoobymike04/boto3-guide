import boto3
import botocore

# Initialize the S3 client with the correct region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

# Upload files
files_to_upload = [
    ('local_file.txt', 'alexboto-new-bucket-1', 'local_file.txt'),
    ('source_file.txt', 'alexboto-new-bucket-1', 'source_file.txt'),
    ('local_file.txt', 'alexboto-new-bucket', 'local_file.txt')
]

for local_file, bucket_name, s3_key in files_to_upload:
    try:
        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"File '{local_file}' uploaded to bucket '{bucket_name}' with key '{s3_key}'.")
    except botocore.exceptions.ClientError as e:
        print(f"Error uploading file '{local_file}' to bucket '{bucket_name}': {e}")
    except botocore.exceptions.EndpointConnectionError as e:
        print(f"Error connecting to the endpoint: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
