import boto3
import json

# Load record data
with open('dns_record.json', 'r') as f:
    record_data = json.load(f)

# Initialize Route 53 client
route53 = boto3.client('route53')

# List record sets in the hosted zone
response = route53.list_resource_record_sets(HostedZoneId=record_data['HostedZoneId'])

# Display record details
record_found = False
for record in response['ResourceRecordSets']:
    if record['Name'] == f"{record_data['RecordName']}." and record['Type'] == record_data['RecordType']:
        print("DNS Record Details:")
        print(f"Name: {record['Name']}")
        print(f"Type: {record['Type']}")
        print(f"TTL: {record['TTL']}")
        print(f"Value: {[r['Value'] for r in record['ResourceRecords']]}")
        record_found = True
        break
if not record_found:
    print("DNS record not found.")