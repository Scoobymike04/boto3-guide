import boto3
import logging

# Setup logging
logging.basicConfig(filename='s3_backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize the S3 resource
s3 = boto3.resource('s3')

source_bucket = 'my-source-bucket-jules'
destination_bucket = 'my-destination-bucket-jules'
copy_source = {
    'Bucket': source_bucket,
    'Key': 'test.txt'
}

try:
    # Copy the object with error handling and logging
    s3.meta.client.copy(copy_source, destination_bucket, 'test.txt')
    logging.info(f"Successfully copied test.txt from {source_bucket} to {destination_bucket}.")
    print("File copied to backup bucket.")
except Exception as e:
    logging.error(f"Error copying file: {e}")
    print(f"Error copying file: {e}")