import boto3
from datetime import datetime

# Initialize the CloudFront client using Boto3
cloudfront = boto3.client('cloudfront')

# Create an invalidation request
response = cloudfront.create_invalidation(
    DistributionId='EXAMPLE_DIST_ID',  # Replace with your actual CloudFront distribution ID
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,  # Number of files/paths to invalidate
            'Items': ['/index.html']  # Specify the path to invalidate
        },
        'CallerReference': f'my-invalidation-{datetime.utcnow().timestamp()}'  # Unique reference to avoid duplicates
    }
)

# Output the Invalidation ID for tracking
print("Invalidation created:", response['Invalidation']['Id'])
