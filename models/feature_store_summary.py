"""
Feature Store summary model.

Stores the outcome of Feature Store operations.
"""

from dataclasses import dataclass


@dataclass
class FeatureStoreSummary:
    """
    Summary of Feature Store operations.
    """

    project_name: str

    entity_name: str

    feature_view: str

    source_table: str

    features_registered: int

    materialization_status: str

    registry_path: str

    def to_dict(self) -> dict:
        """
        Convert the summary to a dictionary.
        """

        return {

            "project_name": self.project_name,

            "entity_name": self.entity_name,

            "feature_view": self.feature_view,

            "source_table": self.source_table,

            "features_registered": self.features_registered,

            "materialization_status": self.materialization_status,

            "registry_path": self.registry_path

        }