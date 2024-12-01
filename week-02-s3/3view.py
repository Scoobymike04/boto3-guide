import boto3 #type: ignore

def configure_website_and_list_files(bucket_name):
    s3_client = boto3.client('s3')
    
    # Enable static website hosting and set index.html as the default document
    s3_client.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            'IndexDocument': {'Suffix': 'index.html'},
            'ErrorDocument': {'Key': 'error.html'}
        }
    )
    
    print(f'Configured {bucket_name} as a static website.')

    # List all objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print('Files in bucket:')
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print('Bucket is empty.')
    
    # Output the public URL for the index.html file
    website_url = f"http://{bucket_name}.s3-website-us-west-2.amazonaws.com/"
    print(f'Public URL for the static website: {website_url}')

if __name__ == "__main__":
    bucket_name = "alex-boto"
    configure_website_and_list_files(bucket_name)