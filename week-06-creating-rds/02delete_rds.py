import boto3

# Initialize the RDS client
rds = boto3.client('rds')

# Delete an RDS instance
response = rds.delete_db_instance(
    DBInstanceIdentifier='mydbinstance',
    SkipFinalSnapshot=True
)

print("RDS instance deleted successfully.")
