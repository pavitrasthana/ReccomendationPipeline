"""
Dataset Version Manager.

Maintains version information for datasets tracked
using Git and Git LFS.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from utils.constants import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FEATURE_DATA_DIR
)


@dataclass
class DatasetVersion:
    """
    Represents a versioned dataset.
    """

    dataset_name: str

    dataset_path: str

    dataset_stage: str

    version: str

    last_updated: str

    tracked_with: str = "Git LFS"


class VersionManager:
    """
    Manages dataset versions.
    """

    def __init__(self):

        self.datasets = []

    def register_dataset(
        self,
        dataset_name: str,
        dataset_path: Path,
        dataset_stage: str,
        version: str = "1.0"
    ):

        dataset = DatasetVersion(

            dataset_name=dataset_name,

            dataset_path=str(dataset_path),

            dataset_stage=dataset_stage,

            version=version,

            last_updated=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

        self.datasets.append(
            dataset
        )

    def register_default_datasets(self):
        """
        Register datasets used in the pipeline.
        """

        self.register_dataset(

            dataset_name="Amazon Raw",

            dataset_path=RAW_DATA_DIR / "amazon",

            dataset_stage="Raw"

        )

        self.register_dataset(

            dataset_name="API Raw",

            dataset_path=RAW_DATA_DIR / "api",

            dataset_stage="Raw"

        )

        self.register_dataset(

            dataset_name="Amazon Processed",

            dataset_path=PROCESSED_DATA_DIR / "amazon",

            dataset_stage="Processed"

        )

        self.register_dataset(

            dataset_name="API Processed",

            dataset_path=PROCESSED_DATA_DIR / "api",

            dataset_stage="Processed"

        )

        self.register_dataset(

            dataset_name="Amazon Features",

            dataset_path=FEATURE_DATA_DIR / "amazon",

            dataset_stage="Feature"

        )

        self.register_dataset(

            dataset_name="API Features",

            dataset_path=FEATURE_DATA_DIR / "api",

            dataset_stage="Feature"

        )

    def get_registered_datasets(self):

        return self.datasets


if __name__ == "__main__":

    manager = VersionManager()

    manager.register_default_datasets()

    print()

    print("Registered Datasets")

    print()

    for dataset in manager.get_registered_datasets():

        print(dataset)