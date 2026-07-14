"""
Recommendation Report Generator.

Generates a recommendation model performance report.
"""

from pathlib import Path

from utils.file_utils import (
    ensure_directory
)


class RecommendationReportGenerator:
    """
    Generates a recommendation model report.
    """

    @staticmethod
    def generate(
        metrics: dict,
        parameters: dict,
        run_id: str,
        output_directory: Path
    ) -> Path:
        """
        Generate recommendation report.
        """

        ensure_directory(
            output_directory
        )

        output_file = (
            output_directory /
            "recommendation_report.txt"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("=" * 80 + "\n")
            file.write("RECOMMENDATION MODEL REPORT\n")
            file.write("=" * 80 + "\n\n")

            file.write(
                "Algorithm : Matrix Factorization (SVD)\n\n"
            )

            file.write("=" * 80 + "\n")
            file.write("MODEL PARAMETERS\n")
            file.write("=" * 80 + "\n\n")

            for key, value in parameters.items():

                file.write(
                    f"{key:<30}: {value}\n"
                )

            file.write("\n")

            file.write("=" * 80 + "\n")
            file.write("MODEL METRICS\n")
            file.write("=" * 80 + "\n\n")

            for key, value in metrics.items():

                if isinstance(
                    value,
                    float
                ):

                    file.write(
                        f"{key:<30}: {value:.4f}\n"
                    )

                else:

                    file.write(
                        f"{key:<30}: {value}\n"
                    )

            file.write("\n")

            file.write("=" * 80 + "\n")
            file.write("MLFLOW\n")
            file.write("=" * 80 + "\n\n")

            file.write(
                f"Run ID : {run_id}\n"
            )

        return output_file