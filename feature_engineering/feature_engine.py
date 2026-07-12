"""
Feature engineering engine.

Coordinates the complete feature engineering workflow.
"""

from __future__ import annotations

import pandas as pd

from feature_engineering.feature_builder import FeatureBuilder
from models.feature_summary import FeatureSummary


class FeatureEngine:
    """
    Executes feature engineering operations using
    the supplied configuration.
    """

    def __init__(self, config):
        """
        Parameters
        ----------
        config : module
            Dataset specific feature engineering configuration.
        """
        self.config = config

    def process(
        self,
        df: pd.DataFrame
    ) -> tuple[pd.DataFrame, FeatureSummary]:
        """
        Execute the complete feature engineering pipeline.

        Parameters
        ----------
        df : pd.DataFrame
            Input dataframe.

        Returns
        -------
        tuple
            Feature engineered dataframe and feature summary.
        """

        rows_before = len(df)
        columns_before = len(df.columns)

        features_created = []

        # --------------------------------------------------
        # Text Length Features
        # --------------------------------------------------

        if self.config.CREATE_TEXT_LENGTH:

            df = FeatureBuilder.add_text_length(
                df,
                self.config.TEXT_COLUMNS
            )

            features_created.extend(
                [
                    f"{column}_length"
                    for column in self.config.TEXT_COLUMNS
                    if column in df.columns
                ]
            )

        # --------------------------------------------------
        # Word Count Features
        # --------------------------------------------------

        if self.config.CREATE_WORD_COUNT:

            df = FeatureBuilder.add_word_count(
                df,
                self.config.TEXT_COLUMNS
            )

            features_created.extend(
                [
                    f"{column}_word_count"
                    for column in self.config.TEXT_COLUMNS
                    if column in df.columns
                ]
            )

        # --------------------------------------------------
        # Amazon Specific Features
        # --------------------------------------------------

        if hasattr(self.config, "CREATE_USER_FEATURES"):

            if self.config.CREATE_USER_FEATURES:

                df = FeatureBuilder.add_user_review_count(
                    df,
                    self.config.USER_COLUMN
                )

                df = FeatureBuilder.add_user_average_rating(
                    df,
                    self.config.USER_COLUMN,
                    self.config.RATING_COLUMN
                )

                features_created.extend(
                    [
                        "user_review_count",
                        "user_average_rating"
                    ]
                )

        if hasattr(self.config, "CREATE_PRODUCT_FEATURES"):

            if self.config.CREATE_PRODUCT_FEATURES:

                df = FeatureBuilder.add_product_review_count(
                    df,
                    self.config.PRODUCT_COLUMN
                )

                df = FeatureBuilder.add_product_average_rating(
                    df,
                    self.config.PRODUCT_COLUMN,
                    self.config.RATING_COLUMN
                )

                features_created.extend(
                    [
                        "product_review_count",
                        "product_average_rating"
                    ]
                )

        # --------------------------------------------------
        # API Specific Features
        # --------------------------------------------------

        if hasattr(self.config, "CREATE_PRICE_BUCKET"):

            if self.config.CREATE_PRICE_BUCKET:

                df = FeatureBuilder.add_price_bucket(
                    df,
                    self.config.PRICE_COLUMN
                )

                features_created.append(
                    "price_bucket"
                )

        if hasattr(self.config, "CREATE_POPULARITY_FEATURE"):

            if self.config.CREATE_POPULARITY_FEATURE:

                df = FeatureBuilder.add_popularity_feature(
                    df,
                    self.config.POPULARITY_COLUMN
                )

                features_created.append(
                    "product_popularity"
                )

        # --------------------------------------------------
        # Summary
        # --------------------------------------------------

        summary = FeatureSummary(

            rows_before=rows_before,

            rows_after=len(df),

            columns_before=columns_before,

            columns_after=len(df.columns),

            features_created=features_created

        )

        return df, summary