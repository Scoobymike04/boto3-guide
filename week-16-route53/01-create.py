import boto3
import json

# Initialize Route 53 client
route53 = boto3.client('route53')

# Set record details
hosted_zone_id = 'Z0376279BNOFSVUO50GJ'
record_name = 'pipeline-build.com'
record_type = 'A'
ttl = 300
record_value = '192.0.2.44'

# Create DNS record
response = route53.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': record_name,
                    'Type': record_type,
                    'TTL': ttl,
                    'ResourceRecords': [{'Value': record_value}]
                }
            }
        ]
    }
)

# Save record to JSON
record_data = {
    'HostedZoneId': hosted_zone_id,
    'RecordName': record_name,
    'RecordType': record_type,
    'TTL': ttl,
    'RecordValue': record_value
}
with open('dns_record.json', 'w') as f:
    json.dump(record_data, f)
print("DNS record created.")