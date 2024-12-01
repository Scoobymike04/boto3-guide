import boto3
import logging

# Setup logging
logging.basicConfig(filename='s3_backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

s3 = boto3.resource('s3')

# Define source and destination buckets (multiple for redundancy)
source_bucket = 'my-source-bucket-jules'
destination_buckets = ['my-destination-bucket-jules', 'my-destination-backup-bucket-jules']  # Multiple buckets
copy_source = {
    'Bucket': source_bucket,
    'Key': 'test.txt'
}

# Loop through the destination buckets for multi-bucket backup
for destination_bucket in destination_buckets:
    try:
        s3.meta.client.copy(copy_source, destination_bucket, 'test.txt')
        logging.info(f"Successfully copied test.txt to {destination_bucket}.")
        print(f"File copied to {destination_bucket}.")
    except Exception as e:
        logging.error(f"Error copying to {destination_bucket}: {e}")
        print(f"Error copying to {destination_bucket}: {e}")