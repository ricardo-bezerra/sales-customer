import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
from databases.mysql_ingestion import Database  # Import the Database class from your module

# Mocking the Config class to provide fake credentials for testing
class MockConfig:
    DB_HOST = 'localhost'
    DB_USER = 'test_user'
    DB_PASSWORD = 'test_password'
    DB_NAME = 'test_db'

@pytest.fixture
def mock_security():
    """Fixture for mocking security-related functionality if needed."""
    return MagicMock()

@pytest.fixture
def mock_mysql_connection():
    """Fixture for mocking a MySQL connection."""
    return MagicMock()

def test_insert_data(mock_security, mock_mysql_connection):
    """Test the insert_data method of the Database class."""
    # Create an instance of the Database object
    database = Database()
    database.security = mock_security  # Injecting the mocked security

    # Create a mock DataFrame with sample data
    data = {
        'name': ['Alicia', 'Roberto'],
        'age': [23, 52],
        'email': ['alicia@test.com', 'roberto@test.com.pt']
    }
    df = pd.DataFrame(data)

    # Mocking the cursor and insert operation
    mock_cursor = MagicMock()
    mock_mysql_connection.cursor.return_value = mock_cursor

    # Patch the connect_mysql method to return the mocked connection
    with patch.object(database, 'connect_mysql', return_value=mock_mysql_connection):
        # Call the insert_data method
        database.insert_data(df, mock_mysql_connection)

    # Ensure the data insertion was called correctly, comparing strings exactly
    expected_sql = "INSERT INTO customer (name, age, email) VALUES (%s, %s, %s)"
    expected_values = [('Alicia', 23, 'alicia@test.com'), ('Roberto', 52, 'roberto@test.com.pt')]
    
    mock_cursor.executemany.assert_called_once_with(expected_sql, expected_values)


def test_create_customer_table(mock_security, mock_mysql_connection):
    """Test the create_customer_table method of the Database class."""
    # Create an instance of the Database object
    database = Database()
    database.security = mock_security  # Injecting the mocked security

    # Mocking the cursor
    mock_cursor = MagicMock()
    mock_mysql_connection.cursor.return_value = mock_cursor

    # Patch the connect_mysql method to return the mocked connection
    with patch.object(database, 'connect_mysql', return_value=mock_mysql_connection):
        # Call the method to create the customer table
        database.create_customer_table(mock_cursor)

    # Ensure the create table query was executed correctly, removing extra spaces and line breaks
    mock_cursor.execute.assert_called_once_with("""
                                                CREATE TABLE IF NOT EXISTS customer (
                                                id INT AUTO_INCREMENT PRIMARY KEY, 
                                                name VARCHAR(255), 
                                                age INT, 
                                                email VARCHAR(255)
                                                );
                                                """.strip())
