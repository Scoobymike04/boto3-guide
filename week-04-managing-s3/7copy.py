import boto3

s3 = boto3.client('s3')

source_bucket_name = 'alexboto-new-bucket-1'
target_bucket_name = 'alexboto-new-bucket-2'
source_key = 'source_file.txt'
target_key = 'target_file.txt'

copy_source = {
    'Bucket': source_bucket_name,
    'Key': source_key
}

# Verify the source key exists in the source bucket
try:
    s3.head_object(Bucket=source_bucket_name, Key=source_key)
    key_exists = True
except Exception as e:
    key_exists = False
    print(f"Error: The key '{source_key}' does not exist in the bucket '{source_bucket_name}'.")

# Proceed with the copy operation if the key exists
if key_exists:
    try:
        s3.copy_object(
            CopySource=copy_source,
            Bucket=target_bucket_name,
            Key=target_key
        )
        print(f"Object '{source_key}' from bucket '{source_bucket_name}' copied to '{target_bucket_name}' with key '{target_key}'.")
    except Exception as e:
        print(f"Error copying object: {e}")
