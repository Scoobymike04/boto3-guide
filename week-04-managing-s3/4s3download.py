import boto3
import botocore

# Initialize the S3 client with the correct region
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)

# Download files
files_to_download = [
    ('alexboto-new-bucket-1', 'local_file.txt', 'local_file_from_bucket_1.txt'),
    ('alexboto-new-bucket', 'local_file.txt', 'local_file_from_bucket.txt')
]

for bucket_name, s3_key, local_file in files_to_download:
    try:
        s3.download_file(bucket_name, s3_key, local_file)
        print(f"File '{s3_key}' downloaded from bucket '{bucket_name}' to local file '{local_file}'.")
    except botocore.exceptions.ClientError as e:
        print(f"Error downloading file '{s3_key}' from bucket '{bucket_name}': {e}")
    except botocore.exceptions.EndpointConnectionError as e:
        print(f"Error connecting to the endpoint: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
