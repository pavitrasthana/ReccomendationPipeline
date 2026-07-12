import great_expectations as gx
import pandas as pd

from config.dataset_config import (
    REQUIRED_COLUMNS,
    RATING_COLUMN,
    RATING_MIN,
    RATING_MAX
)

class GEValidator:
    """
    Great Expectations validation.
    """
    @staticmethod
    def validate(df: pd.DataFrame):
        gx_df = gx.from_pandas(df)
        # Required columns
        for column in REQUIRED_COLUMNS:
            gx_df.expect_column_to_exist(column)
        # Rating exists
        gx_df.expect_column_values_to_not_be_null(
            RATING_COLUMN
        )
        # Rating range
        gx_df.expect_column_values_to_be_between(
            RATING_COLUMN,
            min_value=RATING_MIN,
            max_value=RATING_MAX
        )
        result = gx_df.validate()
        return result.to_json_dict()