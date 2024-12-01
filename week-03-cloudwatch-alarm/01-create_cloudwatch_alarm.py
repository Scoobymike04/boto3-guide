import boto3 #type: ignore

cloudwatch = boto3.client('cloudwatch')

# Create a CloudWatch alarm
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
            'Value': 'i-0cad01eed25279fd4'  # Replace with your instance ID
        },
    ],
    Unit='Percent'
)
print("CloudWatch alarm created.")
