###############################################################################
#                                                                             #
#              THIS SCRIPT ONLY WORKS IF THE BUCKET IS EMPTY                  #
#                                                                             #
###############################################################################

import boto3
from botocore.exceptions import ClientError

from security.security import AWS_BUCKET_NAME_ID, AWS_SECRET_ACCESS_KEY


bucket_name = ""

class S3BucketDeleter:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_resource = boto3.resource(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def delete_bucket(self, bucket_name):
        """
        Deletes the S3 bucket, but only if it is empty.
        """
        bucket = self.s3_resource.Bucket(bucket_name)

        if list(bucket.objects.all()):
            print(f"Bucket '{bucket_name}' is not empty. Cannot delete.")
        else:
            try:
                bucket.delete()
                print(f"Bucket '{bucket_name}' deleted successfully.")
            except ClientError as e:
                print(f"Error: {e}")

# === USAGE ===
ACCESS_KEY = AWS_BUCKET_NAME_ID
SECRET_KEY = AWS_SECRET_ACCESS_KEY
bucket_deleter = S3BucketDeleter(ACCESS_KEY, SECRET_KEY)
bucket_deleter.delete_bucket(bucket_name)
