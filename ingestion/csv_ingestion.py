# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:19:23 2026

@author: pavit
"""

from pathlib import Path
import shutil

import pandas as pd

from config.logger import logger
from utils.constants import RAW_AMAZON_DIR
from utils.file_utils import ensure_directory

class CSVIngestion:
    """
    Handle the ingestion from CSV
    """
    def __init__(self):
        ensure_directory(RAW_AMAZON_DIR)
        self.csv_path = RAW_AMAZON_DIR/"amazon_reviews.csv"
        
    def ingest(self)->pd.DataFrame:
        logger.info("CSV Ingestion Begins...")
        if not self.csv_path.exists():
            logger.error(f"CSV file not found: {self.csv_path}")

            raise FileNotFoundError(self.csv_path)

        df = pd.read_csv(self.csv_path)

        logger.info(f"Rows Loaded : {len(df)}")
        logger.info(f"Columns Loaded : {len(df.columns)}")

        logger.info("CSV ingestion completed successfully.")

        return df