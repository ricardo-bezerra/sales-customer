import pandas as pd
import sys
import os
import pytest

# Add the parent directory of 'data_clean' to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../data_clean')))

# Now import clean_data from the correct module
from data_clean.data_cleaning import clean_data


def test_clean_data():
    # Prepare test data
    raw_data = {
        'name': ['Ricardo Beserra', 'Lusiana Beserra', 'Alícia Bezerra', ' Carlos Lima ', None],
        'age': ['44', '33', 'trinta e cinco', '40', None],
        'email': ['ricardo@email.com', 'luciana@email.com', 'alicia@email.com', 'invalidemail', None]
    }

    df = pd.DataFrame(raw_data)

    # Clean the data
    cleaned_df = clean_data(df)

    # Validate the name cleaning process (whitespace stripped and capitalisation)
    assert cleaned_df['name'].iloc[0] == 'Ricardo Bezerra'
    assert cleaned_df['name'].iloc[1] == 'Luciana Bezerra'
    assert cleaned_df['name'].iloc[2] == 'Alicia Bezerra'
    assert cleaned_df['name'].iloc[3] == 'Carlos Lima'
    assert cleaned_df['name'].iloc[4] == ''

    # Validate age transformation (text to numeric)
    assert cleaned_df['age'].iloc[0] == 44
    assert cleaned_df['age'].iloc[1] == 33
    assert cleaned_df['age'].iloc[2] == 35
    assert cleaned_df['age'].iloc[3] == 40
    assert pd.isna(cleaned_df['age'].iloc[4])

    # Validate email cleaning process
    assert cleaned_df['email'].iloc[0] == 'ricardo@email.com'
    assert cleaned_df['email'].iloc[1] == 'luciana@email.com'
    assert cleaned_df['email'].iloc[2] == 'alicia@email.com'
    assert cleaned_df['email'].iloc[3] == '@'
    assert cleaned_df['email'].iloc[4] == '@'
    
    # Additional edge case: check that non-standard names and age are correctly handled
    test_data = {
        'name': ['Alina Mathews', 'john doe'],
        'age': ['40', 'abc'],
        'email': ['test@test.com', 'john.doe@domain.com']
    }
    df_test = pd.DataFrame(test_data)
    cleaned_test_df = clean_data(df_test)

    assert cleaned_test_df['name'].iloc[0] == 'Alina Mathews'
    assert cleaned_test_df['name'].iloc[1] == 'John Doe'
    assert cleaned_test_df['age'].iloc[0] == 40
    assert pd.isna(cleaned_test_df['age'].iloc[1])
    assert cleaned_test_df['email'].iloc[0] == 'test@test.com'
    assert cleaned_test_df['email'].iloc[1] == 'john.doe@domain.com'
