"""
Shared data transformation utilities.

This module provides reusable transformation
operations that can be applied to any dataset.
"""

import pandas as pd


class DataTransformer:
    """
    Performs generic data transformation operations.
    """

    @staticmethod
    def lowercase_text(
        df: pd.DataFrame,
        columns: list[str],
        enabled: bool = True
    ):
        """
        Convert text columns to lowercase.
        """

        if not enabled:
            return df

        for column in columns:

            if column not in df.columns:
                continue

            df[column] = (
                df[column]
                .astype(str)
                .str.lower()
            )

        return df

    @staticmethod
    def remove_extra_whitespace(
        df: pd.DataFrame,
        columns: list[str],
        enabled: bool = True
    ):
        """
        Remove leading, trailing and
        repeated whitespace.
        """

        if not enabled:
            return df

        for column in columns:

            if column not in df.columns:
                continue

            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
                .str.replace(
                    r"\s+",
                    " ",
                    regex=True
                )
            )

        return df

    @staticmethod
    def convert_dates(
        df: pd.DataFrame,
        columns: list[str]
    ):
        """
        Convert columns to datetime.
        """

        for column in columns:

            if column not in df.columns:
                continue

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

        return df

    @staticmethod
    def convert_dtypes(
        df: pd.DataFrame,
        dtype_mapping: dict
    ):
        """
        Convert dataframe columns
        to specified data types.
        """

        for column, dtype in dtype_mapping.items():

            if column not in df.columns:
                continue

            try:

                df[column] = df[column].astype(dtype)

            except Exception:
                pass

        return df
    
