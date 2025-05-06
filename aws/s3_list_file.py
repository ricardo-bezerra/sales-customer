import boto3

from security.security import AWS_BUCKET_NAME_ID, AWS_SECRET_ACCESS_KEY


bucket_name = ""

class S3FileLister:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def list_files(self, bucket_name, filter_str=''):
        """
        Lists all files in an S3 bucket filtered by substring or extension.
        """
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        files = []
        if 'Contents' in response:
            for obj in response['Contents']:
                key = obj['Key']
                if filter_str in key:
                    files.append(key)
        print(f"Files matching '{filter_str}': {files}")
        return files

# === USAGE ===
ACCESS_KEY = AWS_BUCKET_NAME_ID
SECRET_KEY = AWS_SECRET_ACCESS_KEY
lister = S3FileLister(ACCESS_KEY, SECRET_KEY)
lister.list_files(bucket_name, filter_str=".parquet")
