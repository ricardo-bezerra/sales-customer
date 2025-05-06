import os
import logging
from dotenv import load_dotenv


# Load .env file in the roof Project
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


class Security:
    def __init__(self):
        # MySQL configurations
        self.mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
        self.mysql_user = os.getenv("MYSQL_USER", "root")
        self.mysql_password = os.getenv("MYSQL_PASSWORD")
        if not self.mysql_password:
            raise ValueError("MYSQL_PASSWORD environment variable not set")
        self.mysql_database = os.getenv("MYSQL_DATABASE", "sales")

        # AWS configurations
        self.aws_access_key = os.getenv("AWS_BUCKET_NAME_ID")
        self.aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        if not self.aws_access_key or not self.aws_secret_key:
            raise ValueError("AWS credentials not set in environment")

        self.aws_region = os.getenv("AWS_REGION", "us-east-1")
        self.aws_bucket_name_csv = os.getenv("AWS_BUCKET_NAME_CSV", "csv")
        self.aws_bucket_name_json = os.getenv("AWS_BUCKET_NAME_JSON", "json")
        self.aws_bucket_name_parquet = os.getenv("AWS_BUCKET_NAME_PARQUET", "parquet")

        # Logs configurations
        self.setup_logging()

    def setup_logging(self):
        """ Configuring log """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def validate_credentials(self):
        """ Credentials MySQL and AWS validations"""
        if not all([self.mysql_host, self.mysql_user, self.mysql_password, self.mysql_database]):
            self.logger.error("MySQL credentials or database name are missing")
            return False

        if not all([self.aws_access_key, self.aws_secret_key, self.aws_bucket_name_csv, 
                    self.aws_bucket_name_json, self.aws_bucket_name_parquet]):
            self.logger.error("AWS credentials or bucket name are missing")
            return False
        return True

    def get_mysql_config(self):
        """ MySQL configurations return """
        return {
            "host": self.mysql_host,
            "user": self.mysql_user,
            "password": self.mysql_password,
            "database": self.mysql_database
        }

    def get_aws_s3_config(self):
        """ AWS S3 configurations return """
        return {
            "access_key_id": self.aws_access_key,
            "secret_access_key": self.aws_secret_key,
            "region": self.aws_region,
            "bucket_name_csv": self.aws_bucket_name_csv,
            "bucket_name_json": self.aws_bucket_name_json,
            "bucket_name_parquet": self.aws_bucket_name_parquet
        }
    