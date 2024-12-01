import boto3
from botocore.exceptions import ClientError

def delete_cloudwatch_alarm(alarm_name):
    cloudwatch_client = boto3.client('cloudwatch')
    try:
        # Delete the CloudWatch alarm
        cloudwatch_client.delete_alarms(
            AlarmNames=[alarm_name]
        )
        print(f"Alarm '{alarm_name}' deleted successfully.")
    except ClientError as e:
        print(f"Error deleting alarm '{alarm_name}': {e}")

if __name__ == "__main__":
    alarm_name = "HighCPUUtilization"  # Replace with your alarm name
    delete_cloudwatch_alarm(alarm_name)
