"""
Feature engineering manager for FakeStore API dataset.
"""

import pandas as pd

from config import api_feature_config

from feature_engineering.feature_engine import FeatureEngine
from feature_engineering.feature_report import (
    FeatureReportGenerator
)

from utils.constants import (
    API_PROCESSED_DIR,
    API_FEATURE_DIR,
    API_FEATURE_REPORT_DIR
)

from utils.file_utils import ensure_directory


class APIFeatureManager:
    """
    Executes feature engineering for the
    FakeStore API dataset.
    """

    def run(self):

        # -------------------------------------------------
        # Load latest API dataset
        # -------------------------------------------------

        input_file = (API_PROCESSED_DIR /"products_processed.csv")
        
        df = pd.read_csv(input_file)

        # -------------------------------------------------
        # Execute feature engineering
        # -------------------------------------------------

        engine = FeatureEngine(
            api_feature_config
        )

        feature_df, summary = engine.process(df)

        # -------------------------------------------------
        # Save engineered dataset
        # -------------------------------------------------

        ensure_directory(
            API_FEATURE_DIR
        )

        output_file = (
            API_FEATURE_DIR /
            "products_features.parquet"
        )

        feature_df.to_parquet(
            output_file,
            index=False
        )

        summary.output_file = str(
            output_file
        )

        # -------------------------------------------------
        # Generate report
        # -------------------------------------------------

        report = (
            FeatureReportGenerator.generate(
                summary,
                API_FEATURE_REPORT_DIR
            )
        )

        print()

        print("API feature engineering completed.")

        print(f"Dataset : {output_file}")

        print(f"Report  : {report}")

        return feature_df, summary


if __name__ == "__main__":

    manager = APIFeatureManager()

    manager.run()