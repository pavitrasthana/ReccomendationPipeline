"""
Preprocessing manager for Amazon Reviews dataset.
"""

import pandas as pd

from utils.constants import (
    RAW_AMAZON_DIR,
    PROCESSED_DATA_DIR,
    AMAZON_PREPROCESSING_REPORT_DIR
)

from utils.file_utils import ensure_directory

from config import preprocessing_config

from preprocessing.preprocessing_engine import PreprocessingEngine
from preprocessing.preprocessing_report import (
    PreprocessingReportGenerator
)


class PreprocessingManager:
    """
    Executes preprocessing for the Amazon Reviews dataset.
    """

    def run(self):

        # --------------------------------------------
        # Load dataset
        # --------------------------------------------

        input_file = (
            RAW_AMAZON_DIR /
            "amazon_reviews.csv"
        )

        df = pd.read_csv(input_file)

        # --------------------------------------------
        # Run preprocessing
        # --------------------------------------------

        engine = PreprocessingEngine(
            preprocessing_config
        )

        processed_df, summary = engine.process(df)

        # --------------------------------------------
        # Save processed dataset
        # --------------------------------------------

        output_directory = (
            PROCESSED_DATA_DIR /
            "amazon"
        )

        ensure_directory(output_directory)

        output_file = (
            output_directory /
            "amazon_reviews_processed.csv"
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
                AMAZON_PREPROCESSING_REPORT_DIR
            )
        )

        print()

        print("Amazon preprocessing completed.")

        print(f"Dataset : {output_file}")

        print(f"Report  : {report}")

        return processed_df, summary


if __name__ == "__main__":

    manager = PreprocessingManager()

    manager.run()