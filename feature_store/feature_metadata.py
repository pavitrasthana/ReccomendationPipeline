"""
Feature Metadata Generator.

Generates feature metadata documentation from the
Feature Registry.
"""

import json
from pathlib import Path

from feature_store.feature_registry import (
    FeatureRegistry
)

from utils.file_utils import (
    ensure_directory
)


class FeatureMetadataGenerator:
    """
    Generates feature metadata JSON.
    """

    @staticmethod
    def generate(
        output_directory: Path
    ) -> Path:
        """
        Generate feature metadata JSON.
        """

        ensure_directory(
            output_directory
        )

        registry = FeatureRegistry()

        metadata = {

            "feature_store": "Custom Feature Store",

            "version": "1.0",

            "datasets": {

                "amazon": [

                    feature.__dict__

                    for feature in registry.get_dataset_features(
                        "amazon"
                    )

                ],

                "api": [

                    feature.__dict__

                    for feature in registry.get_dataset_features(
                        "api"
                    )

                ]

            }

        }

        output_file = (
            output_directory /
            "feature_metadata.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4
            )

        return output_file


if __name__ == "__main__":

    from utils.constants import (
        REPORT_DIR
    )

    report = (
        FeatureMetadataGenerator.generate(
            REPORT_DIR /
            "feature_store"
        )
    )

    print()

    print(
        f"Metadata generated:\n{report}"
    )