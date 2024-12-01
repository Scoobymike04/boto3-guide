import boto3
import json

# Load record data
with open('dns_record.json', 'r') as f:
    record_data = json.load(f)

# Initialize Route 53 client
route53 = boto3.client('route53')

# Delete DNS record
response = route53.change_resource_record_sets(
    HostedZoneId=record_data['HostedZoneId'],
    ChangeBatch={
        'Changes': [
            {
                'Action': 'DELETE',
                'ResourceRecordSet': {
                    'Name': record_data['RecordName'],
                    'Type': record_data['RecordType'],
                    'TTL': record_data['TTL'],
                    'ResourceRecords': [{'Value': record_data['RecordValue']}]
                }
            }
        ]
    }
)
print("DNS record deleted.")