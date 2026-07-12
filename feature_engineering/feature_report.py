"""
Feature engineering report generator.

Creates JSON reports describing the feature
engineering operations performed on a dataset.
"""

import json
from pathlib import Path

from utils.file_utils import ensure_directory
from utils.time_utils import get_timestamp


class FeatureReportGenerator:
    """
    Generates feature engineering reports.
    """

    @staticmethod
    def generate(
        summary,
        report_directory: Path
    ) -> Path:
        """
        Generate a feature engineering report.

        Parameters
        ----------
        summary : FeatureSummary
            Summary of feature engineering operations.

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

            "feature_summary": summary.to_dict()

        }

        filename = (
            report_directory /
            f"feature_engineering_{get_timestamp()}.json"
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