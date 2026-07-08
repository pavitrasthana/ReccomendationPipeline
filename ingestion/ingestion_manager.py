# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:34:42 2026

@author: pavit
"""

from config.logger import logger

from ingestion.csv_ingestion import CSVIngestion
from ingestion.api_ingestion import APIIngestion

class IngestionManager:

    def __init__(self):

        self.csv_ingestion = CSVIngestion()

        self.api_ingestion = APIIngestion()

    def run(self):

        logger.info("=" * 60)
        logger.info("STARTING DATA INGESTION PIPELINE")
        logger.info("=" * 60)

        csv_df = self.csv_ingestion.ingest()

        api_df = self.api_ingestion.ingest()

        logger.info("=" * 60)
        logger.info("INGESTION COMPLETED SUCCESSFULLY")
        logger.info("=" * 60)

        return csv_df, api_df


if __name__ == "__main__":

    manager = IngestionManager()

    csv_df, api_df = manager.run()

    print(csv_df.head())

    print(api_df.head())