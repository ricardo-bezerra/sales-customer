class Config:
    def __init__(self):
        self.origin_file = 'origin/customers.csv'
        self.output_csv = 'output/csv/customers_cleaned.csv'
        self.output_json = 'output/json/customers_cleaned.json'
        self.output_parquet = 'output/parquet/customers_cleaned.snappy.parquet'


import os
import logging
from security import env

# Load environment variables from .env file
env()

class Security:
    def __init__(self):
        # MySQL Configuration (localhost)
        self.mysql_host = os.getenv("MYSQL_HOST", "localhost")  # Default is localhost
        self.mysql_user = os.getenv("MYSQL_USER", "root")  # Default user is 'root'
        self.mysql_password = os.getenv("MYSQL_PASSWORD", "root")  # Default password
        self.mysql_database = os.getenv("MYSQL_DATABASE", "sales")  # Default database name

        # AWS S3 Configuration
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID", "")  # AWS Access Key ID
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", "")  # AWS Secret Access Key
        self.aws_region = os.getenv("AWS_REGION", "us-east-1")  # Default region is 'us-east-1'
        self.aws_bucket_name = os.getenv("AWS_BUCKET_NAME", "")  # S3 Bucket name (from env)

        # Logging configuration
        self.setup_logging()

    def setup_logging(self):
        # Setting up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def get_mysql_config(self):
        """ Returns the MySQL configurations """
        return {
            "host": self.mysql_host,
            "user": self.mysql_user,
            "password": self.mysql_password,
            "database": self.mysql_database
        }

    def get_aws_s3_config(self):
        """ Returns the AWS S3 configurations """
        return {
            "access_key_id": self.aws_access_key_id,
            "secret_access_key": self.aws_secret_access_key,
            "region": self.aws_region,
            "bucket_name": self.aws_bucket_name
        }

    def validate(self):
        """ Validate if necessary credentials are set """
        if not all([self.mysql_host, self.mysql_user, self.mysql_password, self.mysql_database]):
            self.logger.error("MySQL credentials are missing.")
            return False
        if not all([self.aws_access_key_id, self.aws_secret_access_key, self.aws_bucket_name]):
            self.logger.error("AWS credentials or bucket name are missing.")
            return False
        return True
