"""
Shared feature creation utilities.

Creates reusable features that can be applied
to multiple datasets.
"""

from __future__ import annotations

import pandas as pd


class FeatureBuilder:
    """
    Generic feature builder.

    Creates derived features from existing columns.
    """

    @staticmethod
    def add_text_length(
        df: pd.DataFrame,
        columns: list[str]
    ) -> pd.DataFrame:
        """
        Add character length features.
        """

        for column in columns:

            if column not in df.columns:
                continue

            df[f"{column}_length"] = (
                df[column]
                .fillna("")
                .astype(str)
                .str.len()
            )

        return df

    @staticmethod
    def add_word_count(
        df: pd.DataFrame,
        columns: list[str]
    ) -> pd.DataFrame:
        """
        Add word count features.
        """

        for column in columns:

            if column not in df.columns:
                continue

            df[f"{column}_word_count"] = (
                df[column]
                .fillna("")
                .astype(str)
                .str.split()
                .str.len()
            )

        return df

    @staticmethod
    def add_user_review_count(
        df: pd.DataFrame,
        user_column: str
    ) -> pd.DataFrame:
        """
        Number of reviews written by each user.
        """

        if user_column not in df.columns:
            return df

        df["user_review_count"] = (
            df.groupby(user_column)[user_column]
            .transform("count")
        )

        return df

    @staticmethod
    def add_user_average_rating(
        df: pd.DataFrame,
        user_column: str,
        rating_column: str
    ) -> pd.DataFrame:
        """
        Average rating given by each user.
        """

        if (
            user_column not in df.columns or
            rating_column not in df.columns
        ):
            return df

        df["user_average_rating"] = (
            df.groupby(user_column)[rating_column]
            .transform("mean")
        )

        return df

    @staticmethod
    def add_product_review_count(
        df: pd.DataFrame,
        product_column: str
    ) -> pd.DataFrame:
        """
        Number of reviews per product.
        """

        if product_column not in df.columns:
            return df

        df["product_review_count"] = (
            df.groupby(product_column)[product_column]
            .transform("count")
        )

        return df

    @staticmethod
    def add_product_average_rating(
        df: pd.DataFrame,
        product_column: str,
        rating_column: str
    ) -> pd.DataFrame:
        """
        Average rating for each product.
        """

        if (
            product_column not in df.columns or
            rating_column not in df.columns
        ):
            return df

        df["product_average_rating"] = (
            df.groupby(product_column)[rating_column]
            .transform("mean")
        )

        return df

    @staticmethod
    def add_price_bucket(
        df: pd.DataFrame,
        price_column: str
    ) -> pd.DataFrame:
        """
        Categorize product prices.
        """

        if price_column not in df.columns:
            return df

        df["price_bucket"] = pd.cut(
            df[price_column],
            bins=[0, 25, 100, float("inf")],
            labels=["Low", "Medium", "High"],
            include_lowest=True
        )

        return df

    @staticmethod
    def add_popularity_feature(
        df: pd.DataFrame,
        popularity_column: str
    ) -> pd.DataFrame:
        """
        Rename popularity column to a
        feature-friendly name.
        """

        if popularity_column not in df.columns:
            return df

        df["product_popularity"] = (
            df[popularity_column]
        )

        return df
    
    @staticmethod
    def add_product_unique_user_count(
        df: pd.DataFrame,
        product_column: str,
        user_column: str
    ) -> pd.DataFrame:
        """
        Number of unique users who reviewed each product.
        """
    
        if (
            product_column not in df.columns or
            user_column not in df.columns
        ):
            return df
    
        df["product_unique_user_count"] = (
            df.groupby(product_column)[user_column]
            .transform("nunique")
        )
    
        return df