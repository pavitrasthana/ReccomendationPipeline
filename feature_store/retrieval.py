"""
Feature Retrieval.

Provides feature retrieval for training and inference.
"""

import pandas as pd

from feature_store.feature_store import (
    FeatureStore
)


class FeatureRetriever:
    """
    Retrieves engineered features from the Feature Store.
    """

    def __init__(self):

        self.store = FeatureStore()

    # =====================================================
    # Training
    # =====================================================

    def get_training_features(
        self,
        dataset: str
    ) -> pd.DataFrame:
        """
        Retrieve features for model training.
        """

        return self.store.get_training_features(
            dataset
        )

    # =====================================================
    # Inference
    # =====================================================

    def get_inference_features(self,dataset: str,entity_id: int) -> pd.DataFrame:
        """
        Retrieve features for a single entity.
        """
    
        df = self.store.get_inference_features(
            dataset
        )
    
        if "id" not in df.columns:
    
            raise KeyError(
                "'id' column not found in feature dataset."
            )
    
        return df[
            df["id"] == entity_id
        ]

    # =====================================================
    # Feature Version
    # =====================================================

    def get_feature_version(
        self,
        feature_name: str
    ):

        return self.store.get_feature_version(
            feature_name
        )

    # =====================================================
    # Available Features
    # =====================================================

    def list_available_features(
        self,
        dataset: str
    ):

        return self.store.list_dataset_features(
            dataset
        )


if __name__ == "__main__":

    retriever = FeatureRetriever()

    print()

    print("========== AMAZON ==========")

    amazon_training = (
        retriever.get_training_features(
            "amazon"
        )
    )

    print(amazon_training.head())

    print()

    print("========== API ==========")

    api_training = (
        retriever.get_training_features(
            "api"
        )
    )

    print(api_training.head())

    print()

    print("========== VERSION ==========")

    print(
        retriever.get_feature_version(
            "title_length"
        )
    )

    print()

    print("========== ENTITY ==========")

    print(
        retriever.get_inference_features(
            "api",
            1
        )
    )