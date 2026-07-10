import pandas as pd

from models.profile_report import ProfileReport
from config.dataset_config import REQUIRED_COLUMNS
from config.dataset_config import *


class DataProfiler:

    """
    Profiles datasets before validation.
    """

    @staticmethod
    def profile(df: pd.DataFrame) -> ProfileReport:

        total_rows = len(df)

        duplicate_count = int(df.duplicated().sum())

        duplicate_percentage = round(
            duplicate_count / total_rows * 100,
            2
        )

        missing_values = (
            df.isnull()
            .sum()
            .astype(int)
            .to_dict()
        )

        missing_percentage = (
            (
                df.isnull()
                .sum()
                / total_rows
                * 100
            )
            .round(2)
            .to_dict()
        )

        unique_values = (
            df.nunique(dropna=True)
            .astype(int)
            .to_dict()
        )

        profile = ProfileReport(

            rows=total_rows,

            columns=len(df.columns),

            memory_usage_mb=float(
                round(
                    df.memory_usage(deep=True).sum()
                    / 1024
                    / 1024,
                    2
                )
            ),

            duplicate_count=duplicate_count,

            duplicate_percentage=duplicate_percentage,

            missing_values=missing_values,

            missing_percentage=missing_percentage,

            unique_values=unique_values,

            data_types=(
                df.dtypes
                .astype(str)
                .to_dict()
            ),

            column_names=df.columns.tolist()

        )

        return profile
    