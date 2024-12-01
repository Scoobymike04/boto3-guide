bucket_name = 'alex-devops-bucket'  # Replace with your bucket name
region = 'us-east-1'  # Ensure this matches the region used
public_url = f'http://{bucket_name}.s3-website-{region}.amazonaws.com'

print(f"Bucket Name: {bucket_name}")
print(f"Public URL: {public_url}")
