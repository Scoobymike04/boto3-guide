import boto3 #type: ignore

def generate_download_links(bucket_name):
    s3_client = boto3.client('s3')
    
    # List all objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print('Download links:')
        for obj in response['Contents']:
            # Generate and print the URL for each object
            file_url = f"https://{bucket_name}.s3.amazonaws.com/{obj['Key']}"
            print(f'{obj["Key"]}: {file_url}')
    else:
        print('Bucket is empty.')

if __name__ == "__main__":
    bucket_name = "alex-boto"
    generate_download_links(bucket_name)