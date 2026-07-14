"""
Data Versioning Manager.

Executes the complete Data Versioning and Lineage workflow.
"""

from data_versioning.version_manager import VersionManager
from data_versioning.lineage_tracker import LineageTracker
from data_versioning.lineage_report import LineageReportGenerator

from utils.constants import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FEATURE_DATA_DIR,
    REPORT_DIR
)


class DataVersioningManager:
    """
    Executes the complete Data Versioning workflow.
    """

    def __init__(self):

        self.version_manager = VersionManager()

        self.lineage_tracker = LineageTracker()

    def run(self):

        datasets = [

            {
                "dataset_name": "Amazon Reviews",
                "dataset_path": RAW_DATA_DIR / "amazon",
                "dataset_stage": "Raw",
                "data_source": "CSV",
                "input_location": "Amazon Reviews Dataset",
                "output_location": str(RAW_DATA_DIR / "amazon"),
                "transformation": "CSV Ingestion"
            },

            {
                "dataset_name": "FakeStore Products",
                "dataset_path": RAW_DATA_DIR / "api",
                "dataset_stage": "Raw",
                "data_source": "REST API",
                "input_location": "https://fakestoreapi.com/products",
                "output_location": str(RAW_DATA_DIR / "api"),
                "transformation": "API Ingestion"
            },

            {
                "dataset_name": "Amazon Processed",
                "dataset_path": PROCESSED_DATA_DIR / "amazon",
                "dataset_stage": "Processed",
                "data_source": "Preprocessing",
                "input_location": str(RAW_DATA_DIR / "amazon"),
                "output_location": str(PROCESSED_DATA_DIR / "amazon"),
                "transformation": "Cleaning + Missing Values + Encoding"
            },

            {
                "dataset_name": "API Processed",
                "dataset_path": PROCESSED_DATA_DIR / "api",
                "dataset_stage": "Processed",
                "data_source": "Preprocessing",
                "input_location": str(RAW_DATA_DIR / "api"),
                "output_location": str(PROCESSED_DATA_DIR / "api"),
                "transformation": "Cleaning + Missing Values"
            },

            {
                "dataset_name": "Amazon Features",
                "dataset_path": FEATURE_DATA_DIR / "amazon",
                "dataset_stage": "Feature",
                "data_source": "Feature Engineering",
                "input_location": str(PROCESSED_DATA_DIR / "amazon"),
                "output_location": str(FEATURE_DATA_DIR / "amazon"),
                "transformation": "Feature Engineering"
            },

            {
                "dataset_name": "API Features",
                "dataset_path": FEATURE_DATA_DIR / "api",
                "dataset_stage": "Feature",
                "data_source": "Feature Engineering",
                "input_location": str(PROCESSED_DATA_DIR / "api"),
                "output_location": str(FEATURE_DATA_DIR / "api"),
                "transformation": "Feature Engineering"
            }

        ]

        for dataset in datasets:

            self.version_manager.register_dataset(

                dataset_name=dataset["dataset_name"],

                dataset_path=dataset["dataset_path"],

                dataset_stage=dataset["dataset_stage"]

            )

            self.lineage_tracker.add_record(

                dataset_name=dataset["dataset_name"],

                dataset_stage=dataset["dataset_stage"],

                data_source=dataset["data_source"],

                input_location=dataset["input_location"],

                output_location=dataset["output_location"],

                transformation=dataset["transformation"]

            )

        lineage_json = self.lineage_tracker.export(

            REPORT_DIR / "data_versioning"

        )

        lineage_report = LineageReportGenerator.generate(

            tracker=self.lineage_tracker,

            output_directory=REPORT_DIR / "data_versioning"

        )

        print()

        print("=" * 60)

        print("DATA VERSIONING & LINEAGE")

        print("=" * 60)

        print()

        print(
            f"Datasets Registered : "
            f"{len(self.version_manager.get_registered_datasets())}"
        )

        print()

        print(f"Lineage JSON   : {lineage_json}")

        print(f"Lineage Report : {lineage_report}")

        print()

        print("Data Versioning completed successfully.")

        return self.version_manager
