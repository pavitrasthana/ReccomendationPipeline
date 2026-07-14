"""
Data Lineage Report Generator.
"""

from pathlib import Path

from data_versioning.lineage_tracker import (
    LineageTracker
)

from utils.file_utils import (
    ensure_directory
)


class LineageReportGenerator:
    """
    Generates a human-readable lineage report.
    """

    @staticmethod
    def generate(
        tracker: LineageTracker,
        output_directory: Path
    ) -> Path:
        """
        Generate the lineage report.
        """

        ensure_directory(output_directory)

        output_file = (
            output_directory /
            "data_lineage_report.txt"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("=" * 80 + "\n")
            file.write("DATA VERSIONING & LINEAGE REPORT\n")
            file.write("=" * 80 + "\n\n")

            for index, record in enumerate(
                tracker.get_records(),
                start=1
            ):

                file.write(f"Record {index}\n")
                file.write("-" * 40 + "\n")

                file.write(
                    f"Dataset              : {record.dataset_name}\n"
                )

                file.write(
                    f"Stage                : {record.dataset_stage}\n"
                )

                file.write(
                    f"Source               : {record.data_source}\n"
                )

                file.write(
                    f"Input                : {record.input_location}\n"
                )

                file.write(
                    f"Output               : {record.output_location}\n"
                )

                file.write(
                    f"Transformation       : {record.transformation}\n"
                )

                file.write(
                    f"Version              : {record.version}\n"
                )

                file.write(
                    f"Ingestion Timestamp  : "
                    f"{record.ingestion_timestamp}\n"
                )

                file.write(
                    f"Generated Timestamp  : "
                    f"{record.generated_timestamp}\n\n"
                )

        return output_file

