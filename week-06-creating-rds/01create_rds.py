import boto3

# Initialize the RDS client
rds = boto3.client('rds')

# Create an RDS instance
response = rds.create_db_instance(
    DBName='database-justjules',
    DBInstanceIdentifier='mydbinstance',  # Unique identifier for the DB instance
    AllocatedStorage=20,                  # Storage size in GB
    DBInstanceClass='db.t2.micro',        # Instance type
    Engine='mysql',                       # Database engine
    MasterUsername='admin',               # Master username
    MasterUserPassword='password',        # Master password
    BackupRetentionPeriod=7,              # Number of days to retain automated backups
    Port=3306                             # Port number to access the DB instance
)

print("RDS instance created successfully.")