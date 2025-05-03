import pandas as pd
import logging


class FileExporter:
    def to_csv(self, df: pd.DataFrame, path: str):
        df.to_csv(path, index=False)
        logging.info(f"Saved CSV to {path}")

    def to_json(self, df: pd.DataFrame, path: str):
        df.to_json(path, orient='records', lines=True)
        logging.info(f"Saved JSON to {path}")

    def to_parquet(self, df: pd.DataFrame, path: str):
        df.to_parquet(path, compression='snappy', index=False)
        logging.info(f"Saved Parquet to {path}")
