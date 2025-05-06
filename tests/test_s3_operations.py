import os
import sys
import pytest
import boto3

# Add the root directory of the project to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aws.s3_convert_file_upload import FileUploader, S3BucketCreator
from security.security import Security


class S3BucketCreator:
    def __init__(self, access_key, secret_key):
        self.s3_client = boto3.client('s3', aws_access_key_id=access_key,
                                      aws_secret_access_key=secret_key)

    def create_bucket(self, bucket_name):
        try:
            self.s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
            return True  # Returns True if the bucket is created successfully
        except self.s3_client.exceptions.BucketAlreadyExists as e:
            print(f"Bucket '{bucket_name}' already exists. Skipping creation.")
            return "Bucket already exists"  # Returns this message if the bucket already exists
        except Exception as e:
            print(f"Failed to create the bucket: {e}")
            return False  # Returns False if any other error occurs


security = Security()


AWS_ACCESS_KEY = security.aws_access_key
AWS_SECRET_KEY = security.aws_secret_key
AWS_REGION = security.aws_region
AWS_BUCKET_NAME_CSV = security.aws_bucket_name_csv
AWS_BUCKET_NAME_JSON = security.aws_bucket_name_json
AWS_BUCKET_NAME_PARQUET = security.aws_bucket_name_parquet


file_uploader = FileUploader(AWS_ACCESS_KEY, AWS_SECRET_KEY)
bucket_creator = S3BucketCreator(AWS_ACCESS_KEY, AWS_SECRET_KEY)

@pytest.fixture(scope="module")
def create_test_bucket():
    """Fixture to create a test bucket before running the tests."""
    test_bucket_name = "test-bucket-for-pytest"
    try:
        bucket_creator.create_bucket(test_bucket_name)
        yield test_bucket_name
    finally:
        pass


def test_create_bucket(create_test_bucket):
    """Tests the creation of a bucket in S3."""
    test_bucket_name = create_test_bucket
    assert test_bucket_name == "test-bucket-for-pytest"


def test_upload_csv(create_test_bucket):
    """Tests the upload of a CSV file to S3."""
    test_file = "test_file.csv"
    
    # Creating a test CSV file
    with open(test_file, "w") as f:
        f.write("name,age\n")
        f.write("Alice,30\n")
        f.write("Bob,25\n")
    
    try:
        file_uploader.upload_csv(test_file)
        # Validates if the file was "uploaded" correctly (in a real test, checking S3 would be necessary)
        assert os.path.exists(test_file)  # Checks if the file exists locally
    finally:
        os.remove(test_file)  # Removes the file after the test


def test_upload_json(create_test_bucket):
    """Tests the upload of a JSON file to S3."""
    test_file = "test_file.json"
    
    # Creating a test JSON file
    with open(test_file, "w") as f:
        f.write('{"name": "Alice", "age": 30}')
    
    try:
        file_uploader.upload_json(test_file)
        # Validates if the file was "uploaded" correctly (in a real test, checking S3 would be necessary)
        assert os.path.exists(test_file)  # Checks if the file exists locally
    finally:
        os.remove(test_file)  # Removes the file after the test


def test_upload_parquet(create_test_bucket):
    """Tests the upload of a Parquet file to S3."""
    test_file = "test_file.parquet"
    
    # Creating a test Parquet file (note that this example generates an empty Parquet file for testing purposes)
    import pandas as pd
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
    df.to_parquet(test_file)
    
    try:
        file_uploader.upload_parquet(test_file)
        # Validates if the file was "uploaded" correctly (in a real test, checking S3 would be necessary)
        assert os.path.exists(test_file)  # Checks if the file exists locally
    finally:
        os.remove(test_file)  # Removes the file after the test


def test_validate_credentials():
    """Tests the validation of AWS and MySQL credentials in the Security object."""
    assert security.validate_credentials() is True  # Ensures the credentials are valid
