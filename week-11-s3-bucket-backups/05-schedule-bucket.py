import schedule #type: ignore
import time
import boto3
import logging

# Setup logging
logging.basicConfig(filename='s3_backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

s3 = boto3.resource('s3')

def backup():
    source_bucket = 'my-source-bucket'
    destination_bucket = 'my-destination-bucket'
    copy_source = {
        'Bucket': source_bucket,
        'Key': 'test.txt'
    }

    try:
        s3.meta.client.copy(copy_source, destination_bucket, 'test.txt')
        logging.info(f"Successfully copied test.txt from {source_bucket} to {destination_bucket}.")
        print("Automated backup complete.")
    except Exception as e:
        logging.error(f"Error during automated backup: {e}")
        print(f"Error during automated backup: {e}")

# Schedule backup every day at midnight
schedule.every().day.at("00:00").do(backup)

# Keep the script running to adhere to schedule
while True:
    schedule.run_pending()
    time.sleep(60)