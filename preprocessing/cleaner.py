"""
Shared data cleaning utilities.

This module provides reusable cleaning operations
that can be applied to any dataset.
"""

import pandas as pd
from datetime import datetime, timezone


class DataCleaner:
    """
    Performs generic data cleaning operations.
    """

    @staticmethod
    def remove_duplicates(
        df: pd.DataFrame,
        remove_duplicates: bool = True
    ):
        """
        Remove duplicate rows.
        """

        before = len(df)

        if remove_duplicates:
            df = df.drop_duplicates()

        removed = before - len(df)

        return df, removed

    @staticmethod
    def drop_missing_rows(
        df: pd.DataFrame,
        required_columns: list[str]
    ):
        """
        Drop rows with missing values
        in the specified columns.
        """

        before = len(df)

        df = df.dropna(
            subset=required_columns
        )

        removed = before - len(df)

        return df, removed

    @staticmethod
    def fill_missing_values(
        df: pd.DataFrame,
        fill_values: dict
    ):
        """
        Fill missing values using the
        provided mapping.
        """

        for column, value in fill_values.items():

            if column in df.columns:

                df[column] = df[column].fillna(value)

        return df

    @staticmethod
    def drop_columns(
        df: pd.DataFrame,
        columns: list[str]
    ):
        """
        Drop unnecessary columns.
        """

        existing_columns = [
            column
            for column in columns
            if column in df.columns
        ]

        df = df.drop(
            columns=existing_columns
        )

        return df