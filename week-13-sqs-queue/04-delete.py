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

    # Receive a message to get its receipt handle for deletion
    receive_response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )

    # Check if a message was received
    if 'Messages' in receive_response:
        message = receive_response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete the message
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
        logging.info("Message deleted.")
    else:
        logging.info("No messages to delete.")

    # Delete the queue
    sqs.delete_queue(QueueUrl=queue_url)
    logging.info(f"Queue deleted: {queue_url}")

except Exception as e:
    logging.error(f"Error deleting message or queue: {e}")
