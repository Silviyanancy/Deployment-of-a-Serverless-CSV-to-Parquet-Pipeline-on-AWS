# Building a Serverless CSV-to-Parquet Pipeline on AWS

This project is to build an automated pipeline that converts CSV files into Parquet format using AWS Services.

The pipeline leverages Amazon S3 for storage, AWS Lambda for event-driven triggers, and AWS Glue for serverless ETL (Extract, Transform, Load).

Step 1: Create S3 Buckets
Bucket1: To store incoming CSV files.
Bucket2: To store processed output Parquet files.

Step 2: Set Up IAM Roles
Role1: Using Lambda as entity - PolicyName: Lambdarole - Attach Policies (AmazonS3FullAccess, AWSGlueConsoleFullAccess)
Role2: Using Glue as entity - PolicyName: Gluerole - Attach Policies (AmazonS3FullAccess, AWSGlueServiceRole)

Step 3: Create AWS Glue Job
Create a job by choosing the job type to be Spark and language to be Python and choose the Gluerole with script (GlueJob.py). 
Set Up the job parameters by setting the path for the input and output bucket (--input_path: s3://bucket1/, --output_path: s3://bucket2/)

Step 4: Create Lambda Function
Create a Lambda function from scratch by choosing the runtime to be Python and Lambdarole.
Use the script (LambdaS3.py)
Add S3 trigger by selcting the bucket1 (where the csv file is) to start the trigger to Glue job when uploaded.

Step 5: Test the Pipeline
Upload a csv to bucket1.
Monitor the Glue job in AWS Glue Console → Jobs → Runs.
Verify Parquet files in bucket2
