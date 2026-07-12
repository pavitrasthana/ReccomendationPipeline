"""
Database loading summary model.

Stores the outcome of the database loading phase.
"""

from dataclasses import dataclass


@dataclass
class DatabaseSummary:
    """
    Summary of database loading operations.
    """

    source_file: str

    target_table: str

    rows_loaded: int

    columns_loaded: int

    load_status: str

    output_database: str

    def to_dict(self) -> dict:
        """
        Convert the summary to a dictionary.
        """

        return {

            "source_file": self.source_file,

            "target_table": self.target_table,

            "rows_loaded": self.rows_loaded,

            "columns_loaded": self.columns_loaded,

            "load_status": self.load_status,

            "output_database": self.output_database

        }