import pandas as pd
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and standardises raw customer data.

    Steps:
    - Strips and capitalises names
    - Manually corrects common name errors
    - Fills missing emails with empty strings
    - Converts 'age' to numeric, replacing invalid entries
    """

    df = df.copy()

    # Removes spaces and capitalises each word
    df['name'] = df['name'].fillna('').str.strip().str.title()

    # Manually corrects common name errors finded at file
    df['name'] = df['name'].replace({
        'Ricardo Beserra': 'Ricardo Bezerra',
        'Lusiana Beserra': 'Luciana Bezerra',
        'Alícia Bezerra': 'Alicia Bezerra'
    })

    # Corrects age written as text into numbers
    df['age'] = df['age'].replace({'trinta e cinco': '35'})

    # Coerce converts all number to data type numeric or NaN
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    # Missing emails are replaced with empty strings
    df['email'] = df['email'].fillna('').str.strip()

    # ~ == Invalid emails (without '@') are replaced with empty '@' string
    df.loc[~df['email'].str.contains('@'), 'email'] = '@'

    logger.info("Data cleaning completed successfully")
    
    return df
