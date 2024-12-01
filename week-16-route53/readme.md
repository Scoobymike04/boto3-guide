Working with Route 53 DNS Records Using AWS GUI and Boto3

This guide explains how to manage DNS records in Route 53 using both the AWS Management Console and Boto3. It includes all necessary prerequisites, step-by-step instructions, and Python scripts to automate DNS management.

Prerequisites
1. Registered Domain Name
Purpose: A registered domain is required to configure DNS records.
Options:
- Register via Route 53:
- Navigate to Route 53 > Registered Domains.
- Click Register Domain, enter your desired domain, and follow the prompts to complete registration.
- Use an Existing Domain:
- Update the domain's nameservers to Route 53's nameservers provided during hosted zone creation.
2. Hosted Zone Creation
Purpose: A hosted zone stores DNS records for a domain.
Steps:
GUI:
- Go to Route 53 > Hosted Zones, click Create Hosted Zone.
- Enter the domain name, choose Public Hosted Zone, and click Create.

Boto3:
import boto3
route53 = boto3.client('route53')

response = route53.create_hosted_zone(
    Name='example.com',
    CallerReference='unique-string',
    HostedZoneConfig={'Comment': 'Hosted zone for example.com', 'PrivateZone': False}
)
print("Hosted Zone ID:", response['HostedZone']['Id'])
Update Nameservers: If using an external registrar, update the nameservers to the ones provided in the Route 53 hosted zone.
3. IAM Permissions
Purpose: Ensure appropriate access to manage Route 53 records.
Custom IAM Policy:
json
Copy code
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "route53:ChangeResourceRecordSets",
        "route53:ListResourceRecordSets",
        "route53:CreateHostedZone",
        "route53:DeleteHostedZone",
        "route53:ListHostedZones"
      ],
      "Resource": "*"
    }
  ]
}

4. AWS CLI and Boto3 Setup
- Install Boto3: Run pip install boto3.
- Configure AWS CLI: Run aws configure to set up credentials and default region.
5. Billing Considerations
- Hosted Zone: $0.50/month per hosted zone.
- Query Costs: $0.40/million queries. Monitor usage to avoid unexpected charges.
6. Optional: SSL Certificates
- Use AWS Certificate Manager (ACM) for free SSL certificates with AWS services like CloudFront.

Part 1: Managing DNS Records Using AWS Management Console
1. Log in to AWS Management Console
- Open AWS Management Console.
- Sign in with your credentials.
2. Navigate to Route 53
- Search for Route 53 in the services search bar and select it.
3. Select Hosted Zone
- Under Hosted Zones, select the one associated with your domain.
4. Create a DNS Record
- Click Create Record.
- Fill in the details:
- Record Name: e.g., www.example.com.
- Record Type: A, CNAME, MX, etc.
- Value: IP address for A records, domain for CNAME, etc.
- TTL: Time-to-live in seconds.
- Click Create records.
5. Delete a DNS Record
- Select the record to delete, click Delete, and confirm.

Part 2: Managing DNS Records Using Boto3
Script 1: Create DNS Record

import boto3
import json

route53 = boto3.client('route53')

# Record details
hosted_zone_id = 'Z1234567890'
record_name = 'www.example.com'
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

# Save record details
with open('dns_record.json', 'w') as f:
    json.dump({
        'HostedZoneId': hosted_zone_id,
        'RecordName': record_name,
        'RecordType': record_type,
        'TTL': ttl,
        'RecordValue': record_value
    }, f)
print("DNS record created.")

Script 2: View DNS Record

import boto3
import json

# Load record data
with open('dns_record.json', 'r') as f:
    record_data = json.load(f)

route53 = boto3.client('route53')

# List records in the hosted zone
response = route53.list_resource_record_sets(HostedZoneId=record_data['HostedZoneId'])
for record in response['ResourceRecordSets']:
    if record['Name'] == f"{record_data['RecordName']}.":
        print(f"Name: {record['Name']}, Type: {record['Type']}, TTL: {record['TTL']}")
        break

Script 3: Update DNS Record

import boto3
import json

# Load record data
with open('dns_record.json', 'r') as f:
    record_data = json.load(f)

route53 = boto3.client('route53')

# Update record
new_ttl = 600
new_value = '192.0.2.45'

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

# Update JSON file
record_data.update({'TTL': new_ttl, 'RecordValue': new_value})
with open('dns_record.json', 'w') as f:
    json.dump(record_data, f)
print("DNS record updated.")

Script 4: List All DNS Records

import boto3

route53 = boto3.client('route53')

hosted_zone_id = 'Z1234567890'
response = route53.list_resource_record_sets(HostedZoneId=hosted_zone_id)

for record in response['ResourceRecordSets']:
    print(f"Name: {record['Name']}, Type: {record['Type']}, TTL: {record.get('TTL', 'N/A')}")

Script 5: Delete DNS Record

import boto3
import json

# Load record data
with open('dns_record.json', 'r') as f:
    record_data = json.load(f)

route53 = boto3.client('route53')

# Delete record
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

Benefits of Automation
- Efficiency: Automates DNS management, reducing manual effort.
- Accuracy: Ensures consistent and error-free configurations.
- Scalability: Easily manage multiple domains and records programmatically.

Costs
- Hosted Zone: $0.50/month per hosted zone.
- DNS Queries: $0.40/million queries.

Conclusion
This guide equips you to manage Route 53 DNS records using both the AWS GUI and Boto3. By automating tasks with Python scripts, you can efficiently handle DNS management for your domains, ensuring flexibility, scalability, and cost-efficiency.






