"""
Custom Feature Store.

Provides access to engineered features stored in PostgreSQL.
"""

import pandas as pd

from config.database import engine

from feature_store.feature_registry import (
    FeatureRegistry
)


class FeatureStore:
    """
    Custom Feature Store for recommendation features.
    """

    def __init__(self):

        self.registry = FeatureRegistry()

    # =====================================================
    # Registry
    # =====================================================

    def list_all_features(self):

        return self.registry.get_all_features()

    def list_dataset_features(
        self,
        dataset: str
    ):

        return self.registry.get_dataset_features(
            dataset
        )

    # =====================================================
    # Feature Retrieval
    # =====================================================

    def load_dataset_features(
        self,
        dataset: str
    ) -> pd.DataFrame:
        """
        Load all engineered features for a dataset.
        """

        if dataset.lower() == "amazon":

            query = """
                SELECT *
                FROM amazon_features
            """

        elif dataset.lower() == "api":

            query = """
                SELECT *
                FROM api_product_features
            """

        else:

            raise ValueError(
                f"Unsupported dataset : {dataset}"
            )

        return pd.read_sql(
            query,
            engine
        )

    # =====================================================
    # Feature Version
    # =====================================================

    def get_feature_version(
        self,
        feature_name: str
    ):

        for feature in self.registry.get_all_features():

            if feature.feature_name == feature_name:

                return feature.version

        return None

    # =====================================================
    # Training Features
    # =====================================================

    def get_training_features(
        self,
        dataset: str
    ) -> pd.DataFrame:
        """
        Returns all features available for training.
        """

        df = self.load_dataset_features(
            dataset
        )

        allowed_features = [

            feature.feature_name

            for feature in self.registry.get_dataset_features(
                dataset
            )

            if feature.available_for_training

        ]

        columns = []

        for column in df.columns:

            if column in allowed_features:

                columns.append(column)

        return df[columns]

    # =====================================================
    # Inference Features
    # =====================================================

    def get_inference_features(
        self,
        dataset: str
    ) -> pd.DataFrame:
        """
        Returns all features available for inference.
        """

        df = self.load_dataset_features(
            dataset
        )

        allowed_features = [

            feature.feature_name

            for feature in self.registry.get_dataset_features(
                dataset
            )

            if feature.available_for_inference

        ]

        columns = []

        for column in df.columns:

            if column in allowed_features:

                columns.append(column)

        return df[columns]


if __name__ == "__main__":

    store = FeatureStore()

    print()

    print(
        f"Registered Features : "
        f"{len(store.list_all_features())}"
    )

    print()

    print(
        "Amazon Features"
    )

    print(
        store.get_training_features(
            "amazon"
        ).head()
    )

    print()

    print(
        "API Features"
    )

    print(
        store.get_training_features(
            "api"
        ).head()
    )