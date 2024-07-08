#AWS S3 File Upload
#This script uploads a file to an AWS S3 bucket.
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_path, bucket_name, s3_file_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, s3_file_name)
        print(f"Upload Successful: {file_path} to bucket {bucket_name} as {s3_file_name}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found")
    except NoCredentialsError:
        print("Credentials not available")

file_path = "path/to/your/file.txt"
bucket_name = "your-s3-bucket"
s3_file_name = "uploaded_file.txt"
upload_to_s3(file_path, bucket_name, s3_file_name)


#############################explaination###################
#Upload Successful: path/to/your/file.txt to bucket your-s3-bucket as uploaded_file.txt
