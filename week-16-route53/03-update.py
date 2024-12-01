import boto3
import json

# Load record data
with open('dns_record.json', 'r') as f:
    record_data = json.load(f)

# Initialize Route 53 client
route53 = boto3.client('route53')

# Define updated values
new_ttl = 600
new_value = '192.0.2.45'

# Update DNS record
response = route53.change_resource_record_sets(
    HostedZoneId=record_data['HostedZoneId'],
    ChangeBatch={
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': record_data['RecordName'],
                    'Type': record_data['RecordType'],
                    'TTL': new_ttl,
                    'ResourceRecords': [{'Value': new_value}]
                }
            }
        ]
    }
)

# Update JSON file with new values
record_data.update({'TTL': new_ttl, 'RecordValue': new_value})
with open('dns_record.json', 'w') as f:
    json.dump(record_data, f)
print("DNS record updated.")