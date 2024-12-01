Managing RDS Instances with AWS GUI and Boto3
Objective
Learn how to create, delete, and manage RDS instances using both the AWS Management Console and Boto3.

Part 1: Managing RDS Instances with the AWS GUI
Step 1: Creating an RDS Instance
- Log in to AWS Management Console: Open the AWS Management Console and log in with your credentials.
- Navigate to RDS: Search for "RDS" in the console and select the RDS service.
- Create a Database: Click "Create database" and select "Standard Create" for more configuration options.
- Select Database Engine: Choose a database engine (e.g., MySQL).
- Configure the Instance:
    DB Identifier: mydbinstance
    Master Username: admin
    Master Password: Set a secure password.
    Instance Type: db.t2.micro
    Storage: 20 GB
Additional Configuration: Optionally configure networking, encryption, backups, and monitoring.
- Create the Database: Click "Create database". The instance status will change to "Available" once the setup is complete.

Step 2: Deleting an RDS Instance
- Navigate to RDS: Go to the RDS Dashboard and select "Databases".
- Select Instance: Choose the instance to delete (e.g., mydbinstance).
- Delete the Instance: Click "Actions" > "Delete".
Confirm Deletion:
- Decide if you want a final snapshot.
- Confirm by typing the required text and click "Delete".
- Outcome: The instance will be deleted and removed from your account.

Part 2: Managing RDS Instances with Boto3
Prerequisites
- Install Boto3: Run pip install boto3.
- Configure AWS CLI: Set up your AWS credentials using aws configure.

Step 1: Creating an RDS Instance with Boto3
File: 01create_rds.py

import boto3

# Initialize the RDS client
rds = boto3.client('rds')

# Create an RDS instance
response = rds.create_db_instance(
    DBName='mydb',
    DBInstanceIdentifier='mydbinstance',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='password',
    BackupRetentionPeriod=7,
    Port=3306
)

print("RDS instance created successfully.")
Instructions:

Save the code above in a file named 01create_rds.py.
Run the script:

python 01create_rds.py
Outcome: A MySQL RDS instance will be created with the specified configuration.

Step 2: Deleting an RDS Instance with Boto3
File: 02delete_rds.py

import boto3

# Initialize the RDS client
rds = boto3.client('rds')

# Delete an RDS instance
response = rds.delete_db_instance(
    DBInstanceIdentifier='mydbinstance',
    SkipFinalSnapshot=True
)

print("RDS instance deleted successfully.")
Instructions:

Save the code above in a file named 02delete_rds.py.
Run the script:

python 02delete_rds.py
Outcome: The specified RDS instance will be deleted without taking a final snapshot.

Summary
This lesson provided step-by-step instructions to manage RDS instances using the AWS GUI and Boto3:
- Create and delete RDS instances via the AWS Management Console.
- Automate RDS management with Python and Boto3 scripts.
