import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

# Initialize the SQS client
sqs = boto3.client('sqs')

# Replace with your actual queue name
queue_name = 'sunday-queue'

try:
    # Create the queue
    response = sqs.create_queue(
        QueueName=queue_name,  # Correct parameter name
        Attributes={
            'DelaySeconds': '1',  # Delay for the message
            'VisibilityTimeout': '30'  # Time to wait before the message is available for another process
        }
    )
    queue_url = response['QueueUrl']
    logging.info(f"Queue was created with the following URL: {queue_url}")
except Exception as e:
    logging.error(f"There was an error creating the queue: {e}")
