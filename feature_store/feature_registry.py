"""
Feature Registry.

Maintains metadata for all engineered features available
for recommendation model training and inference.
"""

from dataclasses import dataclass, asdict
from typing import List


@dataclass
class FeatureDefinition:
    """
    Represents a single engineered feature.
    """

    feature_name: str

    dataset: str

    source_table: str

    source_column: str

    transformation: str

    data_type: str

    version: str

    available_for_training: bool

    available_for_inference: bool


class FeatureRegistry:
    """
    Stores metadata for every registered feature.
    """

    def __init__(self):

        self.features: List[FeatureDefinition] = [

            # =====================================================
            # Amazon Features
            # =====================================================

            FeatureDefinition(
                feature_name="reviews_text_length",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_text",
                transformation="Character Length",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="reviews_text_word_count",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_text",
                transformation="Word Count",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="reviews_title_length",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_title",
                transformation="Character Length",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="reviews_title_word_count",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_title",
                transformation="Word Count",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="user_review_count",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_username",
                transformation="Group By Count",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="user_average_rating",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_rating",
                transformation="Group By Mean",
                data_type="FLOAT",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="product_review_count",
                dataset="amazon",
                source_table="amazon_features",
                source_column="name",
                transformation="Group By Count",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="product_average_rating",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_rating",
                transformation="Group By Mean",
                data_type="FLOAT",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="product_unique_user_count",
                dataset="amazon",
                source_table="amazon_features",
                source_column="reviews_username",
                transformation="Group By NUnique",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            # =====================================================
            # API Features
            # =====================================================

            FeatureDefinition(
                feature_name="title_length",
                dataset="api",
                source_table="api_product_features",
                source_column="title",
                transformation="Character Length",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="title_word_count",
                dataset="api",
                source_table="api_product_features",
                source_column="title",
                transformation="Word Count",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="description_length",
                dataset="api",
                source_table="api_product_features",
                source_column="description",
                transformation="Character Length",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="description_word_count",
                dataset="api",
                source_table="api_product_features",
                source_column="description",
                transformation="Word Count",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="price_bucket",
                dataset="api",
                source_table="api_product_features",
                source_column="price",
                transformation="Price Bucket",
                data_type="STRING",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            ),

            FeatureDefinition(
                feature_name="product_popularity",
                dataset="api",
                source_table="api_product_features",
                source_column="rating_count",
                transformation="Popularity Score",
                data_type="INTEGER",
                version="1.0",
                available_for_training=True,
                available_for_inference=True
            )

        ]

    def get_all_features(self):

        return self.features

    def get_dataset_features(
        self,
        dataset: str
    ):

        return [

            feature

            for feature in self.features

            if feature.dataset == dataset

        ]

    def to_dict(self):

        return [

            asdict(feature)

            for feature in self.features

        ]


if __name__ == "__main__":

    registry = FeatureRegistry()

    print()

    print(f"Registered Features : {len(registry.get_all_features())}")