import boto3

s3 = boto3.resource('s3')

# Define buckets
buckets = ['my-source-bucket-jules', 'my-destination-bucket-jules', 'my-destination-backup-bucket-jules']

# Delete all objects in each bucket
for bucket_name in buckets:
    bucket = s3.Bucket(bucket_name)
    try:
        # Delete objects
        bucket.objects.all().delete()
        print(f"All objects deleted from {bucket_name}.")
        # Delete bucket
        bucket.delete()
        print(f"{bucket_name} bucket deleted.")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")