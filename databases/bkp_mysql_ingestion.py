"""
import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Loading environment variables by .env file
load_dotenv()

# Add parent directory to sys.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def connect_mysql():
    # Connectiong MySQL using environment variables
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        if connection.is_connected():
            print("✅  MySQL database connected")
            return connection
    except Error as e:
        print(f"❌ Error to connect MySQL: {e}")
        return None


def create_customer_table(cursor):
    # Creating table 'customer' if not exists
    create_table_query = """
    """CREATE TABLE IF NOT EXISTS customer (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        email VARCHAR(255)
    );
    """
    """cursor.execute(create_table_query)


def insert_data(df, connection):
    # Inserting cleaned and validated data in 'customer' table in MySQL
    cursor = connection.cursor()
    create_customer_table(cursor)

    insert_query = """
    """INSERT INTO customer (name, age, email) VALUES (%s, %s, %s)
    """
"""
    # Inserting data at MySQL database table
    for _, row in df.iterrows():
        cursor.execute(insert_query, (row['name'], row['age'], row['email']))

    connection.commit()
    print(f"✅ {cursor.rowcount} rows inserted at table 'customer'")

from security.security import Config
cfg = Config()

def main():
    # Main function to data load and table database insert
    # CSV data cleaned and validated path
    # csv_path = os.path.join("output", "csv", "customers_data_cleaned.csv")

    csv_path = cfg.output_csv

    # Verifying the path
    os.makedirs(os.path.join("output", "csv"), exist_ok=True)

    # Verifying if CSV file exists
    if not os.path.exists(csv_path):
        print(f"❌ File {csv_path} not found")
        return
"""
"""    # Loading data cleaned and verified
    df = pd.read_csv(csv_path)
    print(f"✅ {len(df)} registers loaded by {csv_path}.")

    # Conecting MySQL and data inserting in the table
    connection = connect_mysql()
    if connection:
        insert_data(df, connection)
        connection.close()
        print("✅ Connection closed")


if __name__ == "__main__":
    main()
"""