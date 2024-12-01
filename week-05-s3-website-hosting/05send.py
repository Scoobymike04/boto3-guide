import boto3
import botocore

# Initialize the SES client with the correct region
region = 'us-east-1'
ses = boto3.client('ses', region_name=region)

bucket_name = 'alex-devops-bucket'  # Replace with your bucket name
public_url = f'http://{bucket_name}.s3-website-{region}.amazonaws.com'

# Email details
sender_email = 'alexdevopsboto@gmail.com'  # Replace with your verified email address
recipient_email = 'alexdevopsboto@gmail.com'  # Replace with your verified email address
subject = 'S3 Static Website Information'
body_text = (f"Bucket Name: {bucket_name}\n"
             f"Public URL: {public_url}")

# Send the email
try:
    response = ses.send_email(
        Source=sender_email,
        Destination={
            'ToAddresses': [recipient_email]
        },
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body_text}}
        }
    )
    print("Email sent successfully!")
except botocore.exceptions.ClientError as e:
    print(f"Error sending email: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
