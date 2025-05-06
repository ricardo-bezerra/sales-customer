import pandas as pd
from data_clean.data_cleaning import clean_data

from databases.mysql_ingestion import Database

from security.security import Config
cfg = Config()

csv_file = cfg.origin_file


def main():
    try:
        # Read csv
        df = pd.read_csv(csv_file)

        # Data clean and validations
        # Calling clean_data function in the Config class in security
        cleanDF = clean_data(df)

        # Save data cleaned and formated in the correct directory by type file (csv, json and parquet)
        cleanDF.to_csv('output/csv/customers_data_cleaned.csv', index=False)
        cleanDF.to_json('output/json/customers_data_cleaned.json', orient='records', lines=True)
        cleanDF.to_parquet('output/parquet/customers_data_cleaned.snappy.parquet', compression='snappy', index=False)

        print("Data pipeline executed successfully!")

    except Exception as e:
        print(f"Pipeline execution failed with error(s): {e}")

if __name__ == "__main__":
    main()
