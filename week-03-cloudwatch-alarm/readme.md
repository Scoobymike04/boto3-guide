Lesson 04: Setting Up CloudWatch Alarms
Learn how to set up and manage CloudWatch alarms to monitor the health and performance of your AWS resources using both the AWS Management Console and Boto3 in Python.

Part 1: Using the AWS Management Console
Step 1: Creating a CloudWatch Alarm
1. Log in to the AWS Management Console:
   - Navigate to [AWS Management Console](https://aws.amazon.com/console/).
   - Sign in with your credentials.

2. Navigate to CloudWatch Dashboard:
   - In the Services menu, search for and select "CloudWatch".

3. Create an Alarm:
   - In the left-hand menu, click on "Alarms".
   - Click the "Create alarm" button.
   - Click "Select metric".
   - Choose EC2 > Per-Instance Metrics.
   - Select the CPUUtilization metric for your EC2 instance and click "Select metric".

4. Configure the Alarm:
   - Set the following conditions:
     - Threshold type: Static
     - Whenever CPUUtilization is: Greater than
     - Threshold value: 80
     - For: 1 out of 1 datapoints
   - Click "Next".

5. Set Actions (Optional):
   - Optionally configure actions such as notifications when the alarm is triggered.
   - For simplicity, skip this step by clicking "Next".

6. Add a Name and Description:
   - Name: HighCPUUtilization
   - Description: Alarm when server CPU exceeds 80%.

7. Review and Create:
   - Review the alarm configuration.
   - Click "Create alarm".

Part 2: Using Boto3 in Python
Prerequisites

1. Install Boto3: pip install boto3
2. Configure AWS Credentials: aws configure

Step 1: Create a CloudWatch Alarm with Boto3
1. Create a Python Script:
   - Open Visual Studio Code or your preferred IDE.
   - Create a new file: `cloudwatch_alarm.py`.

2. Add the Code:
import boto3

   cloudwatch = boto3.client('cloudwatch')

   Create a CloudWatch alarm
   cloudwatch.put_metric_alarm(
       AlarmName='HighCPUUtilization',
       ComparisonOperator='GreaterThanThreshold',
       EvaluationPeriods=1,
       MetricName='CPUUtilization',
       Namespace='AWS/EC2',
       Period=300,
       Statistic='Average',
       Threshold=80.0,
       ActionsEnabled=False,
       AlarmDescription='Alarm when server CPU exceeds 80%',
       Dimensions=[
           {
               'Name': 'InstanceId',
               'Value': 'i-0abcdef1234567890'  Replace with your EC2 instance ID
           },
       ],
       Unit='Percent'
   )
   print("CloudWatch alarm created.")
3. Run the Script:
   - Open the terminal in Visual Studio Code.
   - Run the script:
python cloudwatch_alarm.py
   - The script creates a CloudWatch alarm for your EC2 instance.

Step 2: Delete a CloudWatch Alarm with Boto3

1. Create a Python Script:
   - Create a new file: `delete_cloudwatch.py`.

2. Add the Code:
import boto3
   from botocore.exceptions import ClientError

   def delete_cloudwatch_alarm(alarm_name):
       cloudwatch_client = boto3.client('cloudwatch')
       try:
           Delete the CloudWatch alarm
           cloudwatch_client.delete_alarms(
               AlarmNames=[alarm_name]
           )
           print(f"Alarm '{alarm_name}' deleted successfully.")
       except ClientError as e:
           print(f"Error deleting alarm '{alarm_name}': {e}")

   if __name__ == "__main__":
       alarm_name = "HighCPUUtilization"  Replace with your alarm name
       delete_cloudwatch_alarm(alarm_name)

3. Run the Script:
   - Open the terminal.
   - Run the script:
python delete_cloudwatch.py
   - The script deletes the specified CloudWatch alarm.

Explanation
1. CloudWatch Alarms:
   - Monitor metrics for AWS resources.
   - Trigger actions based on defined thresholds.

2. Boto3 Integration:
   - Use Python to automate the creation and management of alarms.
   - Simplifies monitoring for scalable and automated workflows.

Summary
In this lesson, you learned to:
1. Set up CloudWatch alarms using the AWS Management Console.
2. Programmatically create and delete CloudWatch alarms using Boto3.

These skills are essential for monitoring AWS resources, ensuring efficient operations, and proactively addressing potential issues.
