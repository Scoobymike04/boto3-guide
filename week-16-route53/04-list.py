import boto3

hosted_zone_id = 'Z0376279BNOFSVUO50GJ'
route53 = boto3.client('route53')

# List all records
response = route53.list_resource_record_sets(HostedZoneId=hosted_zone_id)
for record in response['ResourceRecordSets']:
    print(f"Name: {record['Name']}")
    print(f"Type: {record['Type']}")
    print(f"TTL: {record.get('TTL', 'N/A')}")
    print(f"Value: {[r['Value'] for r in record.get('ResourceRecords', [])]}")
    print("----")