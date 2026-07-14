"""
Database loading report generator.

Creates JSON reports describing the database
loading operations performed on a dataset.
"""

import json
from pathlib import Path

from utils.file_utils import ensure_directory
from utils.time_utils import get_timestamp


class DatabaseReportGenerator:
    """
    Generates database loading reports.
    """

    @staticmethod
    def generate(
        summary,
        report_directory: Path
    ) -> Path:

        ensure_directory(report_directory)

        report = {

            "report_timestamp": get_timestamp(),

            "database_summary": summary.to_dict()

        }

        filename = (
            report_directory
            /
            f"database_load_{get_timestamp()}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str
            )

        return filename