"""
Data Lineage Tracker.

Tracks dataset lineage across the recommendation pipeline.
"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

from utils.file_utils import ensure_directory


@dataclass
class LineageRecord:
    """
    Represents lineage information for a dataset.
    """

    dataset_name: str

    dataset_stage: str

    data_source: str

    input_location: str

    output_location: str

    transformation: str

    version: str

    ingestion_timestamp: str

    generated_timestamp: str


class LineageTracker:
    """
    Maintains dataset lineage throughout the pipeline.
    """

    def __init__(self):

        self.records = []

    def add_record(
        self,
        dataset_name: str,
        dataset_stage: str,
        data_source: str,
        input_location: str,
        output_location: str,
        transformation: str,
        version: str = "1.0"
    ):
        """
        Add a lineage record.
        """

        record = LineageRecord(

            dataset_name=dataset_name,

            dataset_stage=dataset_stage,

            data_source=data_source,

            input_location=input_location,

            output_location=output_location,

            transformation=transformation,

            version=version,

            ingestion_timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            generated_timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

        self.records.append(record)

    def export(
        self,
        output_directory: Path
    ) -> Path:
        """
        Export lineage to JSON.
        """

        ensure_directory(output_directory)

        output_file = (
            output_directory /
            "data_lineage.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                [
                    asdict(record)
                    for record in self.records
                ],

                file,

                indent=4

            )

        return output_file

    def get_records(self):

        return self.records

