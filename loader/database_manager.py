"""
Database loading manager for Amazon Reviews dataset.
"""

import pandas as pd

from loader.database_loader import DatabaseLoader
from loader.database_report import DatabaseReportGenerator

from utils.constants import (
    AMAZON_PROCESSED_DIR,
    AMAZON_FEATURE_DIR,
    AMAZON_DATABASE_REPORT_DIR
)

from config.database_config import (
    AMAZON_PROCESSED_TABLE,
    AMAZON_FEATURE_TABLE
)


class DatabaseManager:

    def run(self):

        loader = DatabaseLoader()

        # -------------------------------------------------
        # Load processed dataset
        # -------------------------------------------------

        processed_file = (
            AMAZON_PROCESSED_DIR /
            "amazon_reviews_processed.csv"
        )

        processed_df = pd.read_csv(
            processed_file
        )

        processed_summary = loader.load_dataframe(
            dataframe=processed_df,
            table_name=AMAZON_PROCESSED_TABLE,
            source_file=processed_file.name
        )

        processed_report = (
            DatabaseReportGenerator.generate(
                processed_summary,
                AMAZON_DATABASE_REPORT_DIR
            )
        )

        # -------------------------------------------------
        # Load feature dataset
        # -------------------------------------------------

        feature_file = (
            AMAZON_FEATURE_DIR /
            "amazon_features.parquet"
        )

        feature_df = pd.read_parquet(
            feature_file
        )

        feature_summary = loader.load_dataframe(
            dataframe=feature_df,
            table_name=AMAZON_FEATURE_TABLE,
            source_file=feature_file.name
        )

        feature_report = (
            DatabaseReportGenerator.generate(
                feature_summary,
                AMAZON_DATABASE_REPORT_DIR
            )
        )

        loader.close()

        print()

        print("Amazon database loading completed.")

        print()

        print(f"Processed Table : {AMAZON_PROCESSED_TABLE}")

        print(f"Features Table  : {AMAZON_FEATURE_TABLE}")

        print()

        print(f"Processed Report : {processed_report}")

        print(f"Feature Report   : {feature_report}")

        return (
            processed_summary,
            feature_summary
        )


if __name__ == "__main__":

    manager = DatabaseManager()

    manager.run()