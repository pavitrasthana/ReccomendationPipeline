# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:29:55 2026

@author: pavit
"""

import json
import requests
import pandas as pd

from config.logger import logger
from utils.constants import RAW_API_DIR, FAKESTORE_API
from utils.file_utils import ensure_directory
from utils.time_utils import get_timestamp
from utils.retry import retry
from utils.time_utils import get_date

class APIIngestion:
    """
    Handles ingestion of product metadata from FakeStore API.
    """

    def __init__(self):

        ensure_directory(RAW_API_DIR)
        self.url = FAKESTORE_API
    @retry(max_attempts=3, delay=2)
    def ingest(self) -> pd.DataFrame:

        logger.info("Starting API ingestion...")

        self.session = requests.Session()        
        response = self.session.get(self.url,timeout=10)

        response.raise_for_status()

        data = response.json()

        timestamp = get_timestamp()

        today_folder =  RAW_API_DIR/get_date()
        ensure_directory(today_folder)          
        output_file = today_folder / f"{timestamp}.json"

        with open(output_file, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4
            )

        logger.info(
            f"Saved API response to {output_file}"
        )

        logger.info(
            f"""
            Source  : FakeStoreAPI
            Rows    : {len(data)}
            Output  : {output_file}
            Status  : SUCCESS
            """
            )

        return pd.DataFrame(data)