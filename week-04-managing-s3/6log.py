import boto3

s3 = boto3.client('s3')

source_bucket_name = 'alexboto-new-bucket-1'
target_bucket_name = 'alexboto-new-bucket-2'

logging_configuration = {
    'LoggingEnabled': {
        'TargetBucket': target_bucket_name,
        'TargetPrefix': 'logs/'
    }
}

try:
    s3.put_bucket_logging(
        Bucket=source_bucket_name,
        BucketLoggingStatus=logging_configuration
    )
    print(f"Logging for bucket '{source_bucket_name}' set up successfully, logs will be stored in '{target_bucket_name}/logs/'.")
except Exception as e:
    print(f"Error setting up logging: {e}")