"""
Feature engineering summary model.

Stores the outcome of the feature engineering phase.
"""

from dataclasses import dataclass, field


@dataclass
class FeatureSummary:
    """
    Summary of feature engineering operations.
    """

    rows_before: int

    rows_after: int

    columns_before: int

    columns_after: int

    features_created: list[str] = field(default_factory=list)

    output_file: str = ""

    def to_dict(self) -> dict:

        return {

            "rows_before": self.rows_before,

            "rows_after": self.rows_after,

            "columns_before": self.columns_before,

            "columns_after": self.columns_after,

            "features_created": self.features_created,

            "output_file": self.output_file

        }