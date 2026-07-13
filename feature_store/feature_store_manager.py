"""
Feature Store Manager.

Executes the complete Feature Store workflow.
"""

from feature_store.feature_store import (
    FeatureStore
)

from feature_store.feature_metadata import (
    FeatureMetadataGenerator
)

from models.feature_store_summary import (
    FeatureStoreSummary
)

from utils.constants import (
    REPORT_DIR
)


class FeatureStoreManager:
    """
    Executes the complete Feature Store workflow.
    """

    def __init__(self):

        self.store = FeatureStore()

    def run(self):
        """
        Execute Feature Store workflow.
        """

        # --------------------------------------------
        # Load Registry
        # --------------------------------------------

        registered_features = (
            self.store.list_all_features()
        )

        # --------------------------------------------
        # Generate Metadata
        # --------------------------------------------

        metadata_file = (
            FeatureMetadataGenerator.generate(
                REPORT_DIR / "feature_store"
            )
        )

        # --------------------------------------------
        # Dataset Statistics
        # --------------------------------------------

        amazon_features = (
            self.store.list_dataset_features(
                "amazon"
            )
        )

        api_features = (
            self.store.list_dataset_features(
                "api"
            )
        )

        # --------------------------------------------
        # Summary
        # --------------------------------------------

        summary = FeatureStoreSummary(

            project_name="RecommendationPipeline",

            entity_name="Products",

            feature_view="Custom Feature Store",

            source_table=(
                "amazon_features, "
                "api_product_features"
            ),

            features_registered=len(
                registered_features
            ),

            materialization_status="SUCCESS",

            registry_path=str(metadata_file)

        )

        print()

        print("=" * 60)

        print("FEATURE STORE")

        print("=" * 60)

        print()

        print(
            f"Registered Features : "
            f"{len(registered_features)}"
        )

        print(
            f"Amazon Features    : "
            f"{len(amazon_features)}"
        )

        print(
            f"API Features       : "
            f"{len(api_features)}"
        )

        print()

        print(
            f"Metadata File : "
            f"{metadata_file}"
        )

        print()

        print("Feature Store completed successfully.")

        print()

        return summary


if __name__ == "__main__":

    manager = FeatureStoreManager()

    manager.run()