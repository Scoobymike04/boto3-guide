import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

# Initialize the SQS client
sqs = boto3.client('sqs')

# Define the queue name
queue_name = 'sunday-queue'

try:
    # Get the queue URL dynamically
    response = sqs.get_queue_url(QueueName=queue_name)
    queue_url = response['QueueUrl']
    logging.info(f"Queue URL retrieved: {queue_url}")

    # Send a message to the queue
    send_response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Hello, SQS world from Sunday class!',
        MessageAttributes={
            'Author': {
                'StringValue': 'Python Developer',
                'DataType': 'String'
            }
        }
    )
    logging.info(f"Message sent: {send_response['MessageId']}")
except Exception as e:
    logging.error(f"Error sending message: {e}")
