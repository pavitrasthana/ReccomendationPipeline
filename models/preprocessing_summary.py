"""
Preprocessing summary model.

Stores the outcome of the preprocessing phase.
"""

from dataclasses import dataclass


@dataclass
class PreprocessingSummary:
    """
    Summary of preprocessing operations.
    """

    rows_before: int

    rows_after: int

    duplicates_removed: int

    missing_rows_removed: int

    columns_removed: list[str]

    processed_columns: list[str]

    output_file: str = ""

    def to_dict(self):

        return {

            "rows_before": self.rows_before,

            "rows_after": self.rows_after,

            "duplicates_removed": self.duplicates_removed,

            "missing_rows_removed": self.missing_rows_removed,

            "columns_removed": self.columns_removed,

            "processed_columns": self.processed_columns,

            "output_file": self.output_file

        }