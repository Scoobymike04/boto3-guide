import boto3
import logging

# Setup logging
logging.basicConfig(filename='s3_backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

s3 = boto3.resource('s3')

source_bucket = 'my-source-bucket-jules'
destination_bucket = 'my-destination-bucket-jules'
copy_source = {
    'Bucket': source_bucket,
    'Key': 'test.txt'
}

# Enable versioning
versioned_copy_key = 'test-versioned.txt'

try:
    s3.meta.client.copy(copy_source, destination_bucket, versioned_copy_key)
    logging.info(f"Versioned copy of test.txt to {versioned_copy_key} in {destination_bucket}.")
    print(f"Versioned file copied as {versioned_copy_key}.")
except Exception as e:
    logging.error(f"Error during versioned copy: {e}")
    print(f"Error during versioned copy: {e}")