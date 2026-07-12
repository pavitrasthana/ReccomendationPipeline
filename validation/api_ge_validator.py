"""
Great Expectations validation for FakeStore API.
"""

import great_expectations as gx
import pandas as pd

from config.api_dataset_config import (
    REQUIRED_COLUMNS,
    PRIMARY_KEY,
    PRICE_COLUMN,
    RATING_COLUMN
)

from config.api_validation_config import (
    PRICE_MIN,
    RATING_MIN,
    RATING_MAX
)


class APIGEValidator:

    @staticmethod
    def validate(df: pd.DataFrame):

        gx_df = gx.from_pandas(df)

        for column in REQUIRED_COLUMNS:

            gx_df.expect_column_to_exist(column)

        gx_df.expect_column_values_to_not_be_null(
            PRIMARY_KEY
        )

        gx_df.expect_column_values_to_be_between(
            PRICE_COLUMN,
            min_value=PRICE_MIN
        )

        gx_df.expect_column_values_to_be_between(
            RATING_COLUMN,
            min_value=RATING_MIN,
            max_value=RATING_MAX
        )

        result = gx_df.validate()

        return result.to_json_dict()