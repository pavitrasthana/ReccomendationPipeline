"""
Preprocessing engine.

Coordinates the complete preprocessing workflow.
"""

from __future__ import annotations

import pandas as pd

from preprocessing.cleaner import DataCleaner
from preprocessing.transformers import DataTransformer

from models.preprocessing_summary import PreprocessingSummary


class PreprocessingEngine:
    """
    Executes preprocessing operations using
    the supplied configuration.
    """

    def __init__(self, config):
        """
        Parameters
        ----------
        config : module
            Dataset specific preprocessing configuration.
        """
        self.config = config

    def process(
        self,
        df: pd.DataFrame
    ) -> tuple[pd.DataFrame, PreprocessingSummary]:
        """
        Execute the complete preprocessing pipeline.

        Parameters
        ----------
        df : pd.DataFrame
            Input dataframe.

        Returns
        -------
        tuple
            Processed dataframe and preprocessing summary.
        """

        rows_before = len(df)

        # --------------------------------------------
        # Remove duplicates
        # --------------------------------------------
        df, duplicates_removed = DataCleaner.remove_duplicates(
            df,
            self.config.REMOVE_DUPLICATES
        )

        # --------------------------------------------
        # Remove rows with missing values
        # --------------------------------------------
        df, missing_rows_removed = DataCleaner.drop_missing_rows(
            df,
            self.config.DROP_ROWS_WITH_MISSING
        )

        # --------------------------------------------
        # Fill missing values
        # --------------------------------------------
        df = DataCleaner.fill_missing_values(
            df,
            self.config.FILL_MISSING_VALUES
        )

        # --------------------------------------------
        # Drop unnecessary columns
        # --------------------------------------------
        df = DataCleaner.drop_columns(
            df,
            self.config.DROP_COLUMNS
        )

        # --------------------------------------------
        # Remove extra whitespace
        # --------------------------------------------
        df = DataTransformer.remove_extra_whitespace(
            df,
            self.config.TEXT_COLUMNS,
            self.config.REMOVE_EXTRA_WHITESPACE
        )

        # --------------------------------------------
        # Convert text to lowercase
        # --------------------------------------------
        df = DataTransformer.lowercase_text(
            df,
            self.config.TEXT_COLUMNS,
            self.config.CONVERT_TO_LOWERCASE
        )

        # --------------------------------------------
        # Convert date columns
        # --------------------------------------------
        df = DataTransformer.convert_dates(
            df,
            self.config.DATE_COLUMNS
        )

        # --------------------------------------------
        # Create preprocessing summary
        # --------------------------------------------
        summary = PreprocessingSummary(
            rows_before=rows_before,
            rows_after=len(df),
            duplicates_removed=duplicates_removed,
            missing_rows_removed=missing_rows_removed,
            columns_removed=self.config.DROP_COLUMNS,
            processed_columns=self.config.TEXT_COLUMNS
        )

        return df, summary