import boto3

from security.security import AWS_BUCKET_NAME_ID, AWS_SECRET_ACCESS_KEY


bucket_name = ""

class S3FileDeleter:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def delete_file(self, bucket_name, file_key):
        """
        Deletes a file from a specified S3 bucket.
        """
        self.s3_client.delete_object(Bucket=bucket_name, Key=file_key)
        print(f"Deleted file '{file_key}' from bucket '{bucket_name}'.")

# === USAGE ===
ACCESS_KEY = AWS_BUCKET_NAME_ID
SECRET_KEY = AWS_SECRET_ACCESS_KEY
deleter = S3FileDeleter(ACCESS_KEY, SECRET_KEY)
deleter.delete_file("bucket_name", "file.parquet")
