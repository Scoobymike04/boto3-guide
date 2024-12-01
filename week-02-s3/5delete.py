import boto3 #type: ignore
from botocore.exceptions import ClientError #type: ignore

def delete_files_and_bucket(bucket_name):
    s3_client = boto3.client('s3')
    
    # List all objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            try:
                # Delete each object in the bucket
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f'Deleted {obj["Key"]} from bucket {bucket_name}.')
            except ClientError as e:
                print(f'Failed to delete {obj["Key"]}: {e}')
    
    # Delete the bucket
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f'Bucket {bucket_name} deleted.')
    except ClientError as e:
        print(f'Failed to delete bucket: {e}')
    
    print('All is deleted.')

if __name__ == "__main__":
    bucket_name = "alex-boto"
    delete_files_and_bucket(bucket_name)