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

    # Receive a message from the queue
    receive_response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,  # Get one message at a time
        WaitTimeSeconds=5,  # Poll for 5 seconds
        MessageAttributeNames=['All']  # Get all message attributes
    )

    # Check if a message was received
    if 'Messages' in receive_response:
        message = receive_response['Messages'][0]
        logging.info(f"Message received: {message['Body']}")

        # Print message attributes
        attributes = message.get('MessageAttributes', {})
        if attributes:
            logging.info(f"Message Attributes: {attributes}")
    else:
        logging.info("No messages received.")

except Exception as e:
    logging.error(f"Error receiving message: {e}")
