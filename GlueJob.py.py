import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    glue.start_job_run(
        JobName='CSV_to_Parquet_Converter',
        Arguments={
            '--input_path': f's3://{bucket}/{key}',
            '--output_path': f's3://processed-parquet-data-awsproject/{key.replace(".csv", "")}'
        }
    )
    return "Glue started to do the job"