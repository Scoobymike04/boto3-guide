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

# Define KMS encryption key for enhanced security
kms_key_id = 'your-kms-key-id'  # Replace with actual KMS key ID

try:
    s3.meta.client.copy(copy_source, destination_bucket, 'test.txt',
                        ExtraArgs={'ServerSideEncryption': 'aws:kms', 'SSEKMSKeyId': kms_key_id})
    logging.info(f"Successfully copied and encrypted test.txt using KMS.")
    print("File copied and encrypted with KMS.")
except Exception as e:
    logging.error(f"Error during KMS encrypted copy: {e}")
    print(f"Error during KMS encrypted copy: {e}")