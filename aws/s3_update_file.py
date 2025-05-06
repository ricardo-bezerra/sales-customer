import boto3

from security.security import AWS_BUCKET_NAME_ID, AWS_SECRET_ACCESS_KEY


bucket_name = ""

class S3FileEditor:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def edit_file(self, bucket_name, file_key, new_content):
        """
        Overwrites file in S3 with new content.
        """
        self.s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=new_content)
        print(f"File '{file_key}' in bucket '{bucket_name}' has been updated.")

# === USAGE ===
ACCESS_KEY = AWS_BUCKET_NAME_ID
SECRET_KEY = AWS_SECRET_ACCESS_KEY
editor = S3FileEditor(ACCESS_KEY, SECRET_KEY)
editor.edit_file(bucket_name, "example.txt", "New content for the file.")
