"""
Preprocessing report generator.

Creates JSON reports describing the preprocessing
operations performed on a dataset.
"""

import json
from pathlib import Path

from utils.file_utils import ensure_directory
from utils.time_utils import get_timestamp


class PreprocessingReportGenerator:
    """
    Generates preprocessing reports.
    """

    @staticmethod
    def generate(
        summary,
        report_directory: Path
    ) -> Path:
        """
        Generate a preprocessing report.

        Parameters
        ----------
        summary : PreprocessingSummary
            Summary of preprocessing operations.

        report_directory : Path
            Directory where the report will be saved.

        Returns
        -------
        Path
            Path to the generated report.
        """

        ensure_directory(report_directory)

        report = {

            "report_timestamp": get_timestamp(),

            "preprocessing_summary": summary.to_dict()

        }

        filename = (
            report_directory
            /
            f"preprocessing_{get_timestamp()}.json"
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