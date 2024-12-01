import boto3 #type: ignore
from botocore.exceptions import ClientError #type: ignore

def upload_files(bucket_name):
    s3_client = boto3.client('s3')
    
    # List of files to upload
    files_to_upload = ['index.html', 'beach.jpg', 'coffee.jpg']
    
    for file in files_to_upload:
        try:
            # Upload the file without setting ACL
            s3_client.upload_file(file, bucket_name, file)
            print(f'Uploaded {file} to bucket {bucket_name}.')
        except ClientError as e:
            print(f'Failed to upload {file}: {e}')

if __name__ == "__main__":
    bucket_name = "alex-boto"
    upload_files(bucket_name)
