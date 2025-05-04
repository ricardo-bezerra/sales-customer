import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

import logging

from security.security import Security
Security()


class Config:
    def __init__(self):
        self.origin_file = 'origin/customers.csv'
        self.output_csv = r"C:\Users\User01\Documents\developer\workspace\data_pipeline\output\csv\customers_data_cleaned.csv"
        self.output_json = 'output/json/customers_data_cleaned.json'
        self.output_parquet = 'output/parquet/customers_data_cleaned.snappy.parquet'


class Database:
    def __init__(self):
        self.config = Config()
        self.security = Security()

    def connect_mysql(self):
        """ Establish connection to MySQL """
        try:
            connection = mysql.connector.connect(
                host=self.security.mysql_host,
                user=self.security.mysql_user,
                password=self.security.mysql_password,
                database=self.security.mysql_database
            )
            if connection.is_connected():
                print("✅ Successfully connected to MySQL database.")
                return connection
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            return None

    def create_customer_table(self, cursor):
        """ Create 'customer' table in MySQL if it doesn't already exist """
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
        """ Insert data from the cleaned CSV DataFrame into the MySQL 'customer' table """
        cursor = connection.cursor()
        self.create_customer_table(cursor)

        insert_query = """
        INSERT INTO customer (name, age, email) VALUES (%s, %s, %s)
        """

        for _, row in df.iterrows():
            cursor.execute(insert_query, (row['name'], row['age'], row['email']))

        connection.commit()
        print(f"✅ {cursor.rowcount} rows inserted into 'customer' table.")

    def close_connection(self, connection):
        """ Close the MySQL connection """
        connection.close()
        print("✅ MySQL connection closed.")


# Main ingestion script
def main():
    # Load cleaned data from the CSV file
    csv_path = os.path.join("output", "csv", "customers_data_cleaned.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    if not os.path.exists(csv_path):
        print(f"❌ File {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    print(f"✅ {len(df)} registers loaded from {csv_path}.")

    # Connect to MySQL
    database = Database()
    connection = database.connect_mysql()

    if connection:
        database.insert_data(df, connection)
        database.close_connection(connection)


if __name__ == "__main__":
    main()
