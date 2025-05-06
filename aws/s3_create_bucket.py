import boto3

from security.security import Security
security = Security()
access_key = security.aws_access_key_id


AWS_BUCKET_NAME_ID = security.aws_access_key_id
AWS_SECRET_ACCESS_KEY = security.aws_secret_access_key



# Data Ingestion - Multiple Files - Bucket
bucket_name = "di-mf-bucket"

class S3BucketCreator:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def create_bucket(self, bucket_name):
        """
        Creates a new S3 bucket.
        """
        try:
            self.s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        except Exception as e:
            print(f"Failed to create bucket: {e}")

# === USAGE ===
# Replace with your AWS credentials
ACCESS_KEY = AWS_BUCKET_NAME_ID
SECRET_KEY = AWS_SECRET_ACCESS_KEY

# === USAGE ===
if __name__ == "__main__":
    ACCESS_KEY = AWS_BUCKET_NAME_ID
    SECRET_KEY = AWS_SECRET_ACCESS_KEY

    bucket_creator = S3BucketCreator(ACCESS_KEY, SECRET_KEY)
    bucket_creator.create_bucket(bucket_name)
