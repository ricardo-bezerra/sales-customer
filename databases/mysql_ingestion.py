import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import logging

# Load environment variables from the .env file
load_dotenv()

from security.security import Security


# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration class for file paths
class Config:
    def __init__(self):
        self.origin_file = 'origin/customers.csv'
        self.output_csv = r"C:\Users\User01\Documents\developer\workspace\data_pipeline\output\csv\customers_data_cleaned.csv"
        self.output_json = 'output/json/customers_data_cleaned.json'
        self.output_parquet = 'output/parquet/customers_data_cleaned.snappy.parquet'


# Database interaction class for MySQL
class Database:
    def __init__(self):
        self.config = Config()
        self.security = Security()

    def connect_mysql(self):
        """ Establishes the connection to MySQL """
        try:
            connection = mysql.connector.connect(
                host=self.security.mysql_host,
                user=self.security.mysql_user,
                password=self.security.mysql_password,
                database=self.security.mysql_database
            )
            if connection.is_connected():
                logging.info("✅ Successfully connected to MySQL database.")
                return connection
        except Error as e:
            logging.error(f"❌ Error connecting to MySQL: {e}")
            return None

    def create_customer_table(self, cursor):
        """ Creates the 'customer' table in MySQL if it doesn't already exist """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            email VARCHAR(255)
        );
        """
        cursor.execute(create_table_query)

    def insert_data(self, df, connection):
        """ Inserts data from the cleaned CSV into the MySQL 'customer' table """
        cursor = connection.cursor()
        self.create_customer_table(cursor)

        insert_query = """
        INSERT INTO customer (name, age, email) VALUES (%s, %s, %s)
        """

        data_to_insert = [(row['name'], row['age'], row['email']) for _, row in df.iterrows()]

        try:
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            logging.info(f"✅ {cursor.rowcount} rows inserted into 'customer' table.")
        except Error as e:
            logging.error(f"❌ Error inserting data into MySQL: {e}")
            connection.rollback()

    def close_connection(self, connection):
        """ Closes the MySQL connection """
        connection.close()
        logging.info("✅ MySQL connection closed.")


# Main ingestion function
def main():
    # Load the cleaned data from the CSV file
    csv_path = os.path.join("output", "csv", "customers_data_cleaned.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    if not os.path.exists(csv_path):
        logging.error(f"❌ File {csv_path} not found.")
        return

    try:
        df = pd.read_csv(csv_path)
        logging.info(f"✅ {len(df)} records loaded from {csv_path}.")
    except Exception as e:
        logging.error(f"❌ Error reading CSV file: {e}")
        return

    # Connect to MySQL
    database = Database()
    connection = database.connect_mysql()

    if connection:
        database.insert_data(df, connection)
        database.close_connection(connection)


if __name__ == "__main__":
    main()

