"""
Feature engineering manager for Amazon Reviews dataset.
"""

from pathlib import Path

import pandas as pd

from config import feature_config

from feature_engineering.feature_engine import FeatureEngine
from feature_engineering.feature_report import (
    FeatureReportGenerator
)

from utils.constants import (
    AMAZON_PROCESSED_DIR,
    AMAZON_FEATURE_DIR,
    AMAZON_FEATURE_REPORT_DIR
)

from utils.file_utils import ensure_directory


class FeatureManager:
    """
    Executes feature engineering for the
    Amazon Reviews dataset.
    """

    def run(self):

        # -------------------------------------------------
        # Load processed dataset
        # -------------------------------------------------

        input_file = (
            AMAZON_PROCESSED_DIR /
            "amazon_reviews_processed.csv"
        )

        df = pd.read_csv(input_file)

        # -------------------------------------------------
        # Execute feature engineering
        # -------------------------------------------------

        engine = FeatureEngine(
            feature_config
        )

        feature_df, summary = engine.process(df)

        # -------------------------------------------------
        # Save engineered dataset
        # -------------------------------------------------

        ensure_directory(
            AMAZON_FEATURE_DIR
        )

        output_file = (
            AMAZON_FEATURE_DIR /
            "amazon_features.parquet"
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
                AMAZON_FEATURE_REPORT_DIR
            )
        )

        print()

        print("Amazon feature engineering completed.")

        print(f"Dataset : {output_file}")

        print(f"Report  : {report}")

        return feature_df, summary


if __name__ == "__main__":

    manager = FeatureManager()

    manager.run()