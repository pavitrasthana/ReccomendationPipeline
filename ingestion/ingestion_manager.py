# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:34:42 2026

@author: pavit
"""

from utils.report_utils import save_pipeline_metadata
from config.logger import logger
import traceback

from ingestion.csv_ingestion import CSVIngestion
from ingestion.api_ingestion import APIIngestion

from utils.time_utils import(
    get_timestamp,
    generate_run_id
    )

class IngestionManager:

    def __init__(self):

        self.csv_ingestion = CSVIngestion()

        self.api_ingestion = APIIngestion()

    def run(self):
        pipeline_metadata = {
                "pipeline_run_id": generate_run_id(),
                "pipeline_name": "RecommendationPipeline",
                "timestamp": get_timestamp(),
                "status": "RUNNING",
                "sources": []
                }
        
        logger.info("=" * 60)
        logger.info("STARTING DATA INGESTION PIPELINE")
        logger.info("=" * 60)

        try:
            csv_df, csv_metadata = self.csv_ingestion.ingest()
            pipeline_metadata["sources"].append(csv_metadata)
            api_df, api_metadata = self.api_ingestion.ingest()
            pipeline_metadata["sources"].append(api_metadata)
            pipeline_metadata["status"] = "SUCCESS"
            logger.info("=" * 60)
            logger.info("INGESTION COMPLETED SUCCESSFULLY")
            logger.info("=" * 60)
        except Exception as e:
            pipeline_metadata["status"] = "FAILED"
            pipeline_metadata["error"] = str(e)
            pipeline_metadata["traceback"] = traceback.format_exc()
            logger.exception("Pipeline execution failed.")
            raise
        finally:
            filename = (f"pipeline_{pipeline_metadata['timestamp']}.json")
            report = save_pipeline_metadata(pipeline_metadata,filename)
            logger.info(f"Pipeline metadata saved to {report}")
            return csv_df, api_df


if __name__ == "__main__":

    manager = IngestionManager()

    csv_df, api_df = manager.run()

    print(csv_df.head())

    print(api_df.head())