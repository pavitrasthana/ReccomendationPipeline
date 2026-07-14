"""
Database loading manager for FakeStore API dataset.
"""

import pandas as pd

from loader.database_loader import DatabaseLoader
from loader.database_report import DatabaseReportGenerator

from utils.constants import (
    API_PROCESSED_DIR,
    API_FEATURE_DIR,
    API_DATABASE_REPORT_DIR
)

from config.database_config import (
    API_PROCESSED_TABLE,
    API_FEATURE_TABLE
)


class APIDatabaseManager:

    def run(self):
        """
        Execute database loading workflow.
        """

        loader = DatabaseLoader()

        # -------------------------------------------------
        # Load processed dataset
        # -------------------------------------------------

        processed_file = (
            API_PROCESSED_DIR /
            "products_processed.csv"
        )

        processed_df = pd.read_csv(
            processed_file
        )

        processed_summary = loader.load_dataframe(
            dataframe=processed_df,
            table_name=API_PROCESSED_TABLE,
            source_file=processed_file.name
        )

        processed_report = (
            DatabaseReportGenerator.generate(
                processed_summary,
                API_DATABASE_REPORT_DIR
            )
        )

        # -------------------------------------------------
        # Load feature dataset
        # -------------------------------------------------

        feature_file = (
            API_FEATURE_DIR /
            "products_features.parquet"
        )

        feature_df = pd.read_parquet(
            feature_file
        )

        feature_summary = loader.load_dataframe(
            dataframe=feature_df,
            table_name=API_FEATURE_TABLE,
            source_file=feature_file.name
        )

        feature_report = (
            DatabaseReportGenerator.generate(
                feature_summary,
                API_DATABASE_REPORT_DIR
            )
        )

        loader.close()

        print()

        print("API database loading completed.")

        print()

        print(f"Processed Table : {API_PROCESSED_TABLE}")

        print(f"Features Table  : {API_FEATURE_TABLE}")

        print()

        print(f"Processed Report : {processed_report}")

        print(f"Feature Report   : {feature_report}")

        return (
            processed_summary,
            feature_summary
        )


if __name__ == "__main__":

    manager = APIDatabaseManager()

    manager.run()