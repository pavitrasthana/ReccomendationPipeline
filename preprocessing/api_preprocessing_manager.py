"""
Preprocessing manager for FakeStore API.
"""

import json
from datetime import datetime, timezone

import pandas as pd

from utils.api_utils import get_latest_api_file

from utils.constants import (
    RAW_API_DIR,
    PROCESSED_DATA_DIR,
    API_PREPROCESSING_REPORT_DIR
)

from utils.file_utils import ensure_directory

from config import api_preprocessing_config

from preprocessing.preprocessing_engine import (
    PreprocessingEngine
)

from preprocessing.preprocessing_report import (
    PreprocessingReportGenerator
)


class APIPreprocessingManager:
    """
    Executes preprocessing for FakeStore API.
    """

    def run(self):

        # --------------------------------------------
        # Locate latest API file
        # --------------------------------------------

        latest_file = get_latest_api_file(
            RAW_API_DIR
        )

        with open(
            latest_file,
            "r",
            encoding="utf-8"
        ) as file:

            products = json.load(file)

        df = pd.json_normalize(products)

        # --------------------------------------------
        # Run preprocessing
        # --------------------------------------------

        engine = PreprocessingEngine(
            api_preprocessing_config
        )

        processed_df, summary = engine.process(df)

        # --------------------------------------------
        # Add ingestion timestamp
        # --------------------------------------------

        ingestion_time = datetime.now(timezone.utc)

        processed_df["ingestion_timestamp"] = (
            ingestion_time
        )

        # --------------------------------------------
        # Save processed dataset
        # --------------------------------------------

        output_directory = (
            PROCESSED_DATA_DIR /
            "api"
        )

        ensure_directory(output_directory)

        output_file = (
            output_directory /
            "products_processed.csv"
        )

        processed_df.to_csv(
            output_file,
            index=False
        )

        summary.output_file = str(output_file)

        # --------------------------------------------
        # Generate report
        # --------------------------------------------

        report = (
            PreprocessingReportGenerator.generate(
                summary,
                API_PREPROCESSING_REPORT_DIR
            )
        )

        print()

        print("API preprocessing completed.")

        print(f"Dataset : {output_file}")

        print(f"Report  : {report}")

        return processed_df, summary


if __name__ == "__main__":

    manager = APIPreprocessingManager()

    manager.run()