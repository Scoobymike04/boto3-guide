import json
import boto3 #type: ignore
from botocore.exceptions import ClientError #type: ignore

def create_s3_bucket(bucket_name):
    region = 'us-west-2'
    s3_client = boto3.client('s3', region_name=region)
    
    # Create the bucket with a specific location constraint
    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f'Bucket {bucket_name} created.')
    except ClientError as e:
        print(f'Error creating bucket: {e}')
        return
    
    # Disable public access blocking
    s3_client.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )
    
    # Set bucket policy to allow public read access
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject",
                    "s3:ListBucket"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}",
                    f"arn:aws:s3:::{bucket_name}/*"
                ]
            }
        ]
    }
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))
    
    print(f'Bucket {bucket_name} is now publicly accessible.')

if __name__ == "__main__":
    bucket_name = "alex-boto"
    create_s3_bucket(bucket_name)