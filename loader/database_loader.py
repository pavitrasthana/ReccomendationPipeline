"""
Database loader.

Provides reusable functionality for loading
pandas DataFrames into PostgreSQL.
"""

import pandas as pd

from config.database import engine
from config.config import POSTGRES_DB

from config.database_config import (
    IF_EXISTS,
    INDEX,
    CHUNK_SIZE
)

from models.database_summary import DatabaseSummary


class DatabaseLoader:
    """
    Generic PostgreSQL database loader.
    """

    def __init__(self):
        """
        Initialize the database loader using
        the shared SQLAlchemy engine.
        """

        self.engine = engine

    def load_dataframe(
        self,
        dataframe: pd.DataFrame,
        table_name: str,
        source_file: str
    ) -> DatabaseSummary:
        """
        Load a dataframe into PostgreSQL.
        """

        dataframe.to_sql(
            name=table_name,
            con=self.engine,
            if_exists=IF_EXISTS,
            index=INDEX,
            chunksize=CHUNK_SIZE
        )

        summary = DatabaseSummary(
            source_file=source_file,
            target_table=table_name,
            rows_loaded=len(dataframe),
            columns_loaded=len(dataframe.columns),
            load_status="SUCCESS",
            output_database=POSTGRES_DB
        )

        return summary

    def close(self):
        """
        Dispose the shared database engine.
        """

        self.engine.dispose()