import os
import logging
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Security:
    def __init__(self):
        # MySQL Configuration
        self.mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
        self.mysql_user = os.getenv("MYSQL_USER", "root")
        self.mysql_password = os.getenv("MYSQL_PASSWORD")
        if not self.mysql_password:
            raise ValueError("MYSQL_PASSWORD environment variable not set")
        self.mysql_database = os.getenv("MYSQL_DATABASE", "sales")

        # AWS Configuration
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID", "")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", "")
        self.aws_region = os.getenv("AWS_REGION", "")
        self.aws_bucket_name_csv = os.getenv("AWS_BUCKET_NAME_CSV", "")
        self.aws_bucket_name_json = os.getenv("AWS_BUCKET_NAME_JSON", "")
        self.aws_bucket_name_parquet = os.getenv("AWS_BUCKET_NAME_PARQUET", "")

        # Logging configuration
        self.setup_logging()

    def setup_logging(self):
        """ Set up logging """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def validate_credentials(self):
        """ Validate MySQL and AWS credentials """
        if not all([self.mysql_host, self.mysql_user, self.mysql_password, self.mysql_database]):
            self.logger.error("MySQL credentials or database name are missing")
            return False
        
        if not all([self.aws_access_key_id, self.aws_secret_access_key, self.aws_bucket_name_csv, 
                    self.aws_bucket_name_json, self.aws_bucket_name_parquet]):
            self.logger.error("AWS credentials or bucket name are missing")
            return False
        return True

    def get_mysql_config(self):
        """ Returns MySQL configuration details """
        return {
            "host": self.mysql_host,
            "user": self.mysql_user,
            "password": self.mysql_password,
            "database": self.mysql_database
        }

    def get_aws_s3_config(self):
        """ Returns AWS S3 configuration details """
        return {
            "access_key_id": self.aws_access_key_id,
            "secret_access_key": self.aws_secret_access_key,
            "region": self.aws_region,
            "bucket_name_csv": self.aws_bucket_name_csv,
            "bucket_name_json": self.aws_bucket_name_json,
            "bucket_name_parquet": self.aws_bucket_name_parquet
        }


"""
Paths files Project:

Relative path or can be changed to absolute path (not recommended)


class Config:
    def __init__(self):
        self.origin_file = 'origin/customers.csv'
        # self.output_csv = 'output/csv/customers_data_cleaned.csv'
        self.output_csv = r"C:\Users\User01\Documents\developer\workspace\data_pipeline\output\csv\customers_data_cleaned.csv"
        self.output_json = 'output/json/customers_data_cleaned.json'
        self.output_parquet = 'output/parquet/customers_data_cleaned.snappy.parquet'


import os
import logging
from dotenv import load_dotenv
load_dotenv()

# Mysql configuration
class Security:
    def __init__(self):
        # Configuration (localhost)
        # Default is localhost (host, IP, etc)
        self.mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
        # Database user
        self.mysql_user = os.getenv("MYSQL_USER", "root")
        # Database password (from env)
        self.mysql_password = os.getenv("MYSQL_PASSWORD")
        if not self.mysql_password:
            raise ValueError("MYSQL_PASSWORD environment variable not set")
        self.mysql_database = os.getenv("MYSQL_DATABASE", "sales")


        # AWS S3 Configuration
        # AWS Access Key ID
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID", "")
        # AWS Secret Access Key
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", "")
        # Default region is 'us-east-1'
        self.aws_region = os.getenv("AWS_REGION", "")
        # S3 Bucket name csv (from env)
        self.aws_bucket_name_csv = os.getenv("AWS_BUCKET_NAME_CSV", "")
        # S3 Bucket name json (from env)
        self.aws_bucket_name_json = os.getenv("AWS_BUCKET_NAME_JSON", "")
        # S3 Bucket name parquet (from env)
        self.aws_bucket_name_parquet = os.getenv("AWS_BUCKET_NAME_PARQUET", "")


        # Logging configuration
        self.setup_logging()

    def setup_logging(self):
        # Setting up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def get_mysql_config(self):
        # Returns the MySQL configurations
        return {
            "host": self.mysql_host,
            "user": self.mysql_user,
            "password": self.mysql_password,
            "database": self.mysql_database
        }
"""
"""
    def get_aws_s3_config(self):
        # Returns the AWS S3 configurations
        return {
            "access_key_id": self.aws_access_key_id,
            "secret_access_key": self.aws_secret_access_key,
            "region": self.aws_region,
            "bucket_name_csv": self.aws_bucket_name_csv,
            "bucket_name_json": self.aws_bucket_name_json,
            "bucket_name_parquet": self.aws_bucket_name_parquet
        }

    def validate_credentials(self):
        # Validate if necessary credentials are set
        if not all([self.mysql_host, self.mysql_user, self.mysql_password, self.mysql_database]):
            self.logger.error("MySQL credentials or database name are missing")
            return False
        
        if not all([self.aws_access_key_id, self.aws_secret_access_key, self.aws_bucket_name_csv, 
                    self.aws_bucket_name_json, self.aws_bucket_name_parquet]):
            self.logger.error("AWS credentials or bucket name are missing")
            return False
        return True
"""