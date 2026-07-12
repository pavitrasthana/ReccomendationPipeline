# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:38:22 2026

@author: pavit
"""

from pathlib import Path
PROJECT_ROOT=Path(__file__).resolve().parent.parent

#Other Directories
DATA_DIR=PROJECT_ROOT/"data"
RAW_DATA_DIR=DATA_DIR/"raw"
RAW_AMAZON_DIR=RAW_DATA_DIR/"amazon"
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
RAW_AMAZON_DIR = RAW_DATA_DIR / "amazon"
RAW_API_DIR = RAW_DATA_DIR / "api"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
VALIDATED_DIR = DATA_DIR / "validated"
FEATURE_DIR = DATA_DIR / "features"
REPORT_DIR = PROJECT_ROOT/"reports"
INGESTION_REPORT_DIR = REPORT_DIR/"ingestion"
VALIDATION_REPORT_DIR = REPORT_DIR / "validation"
RAW_API_DIR = RAW_DATA_DIR / "api"

PREPROCESSING_REPORT_DIR = REPORT_DIR / "preprocessing"

AMAZON_PREPROCESSING_REPORT_DIR = PREPROCESSING_REPORT_DIR / "amazon"

API_PREPROCESSING_REPORT_DIR = PREPROCESSING_REPORT_DIR / "api"

AMAZON_PROCESSED_DIR = PROCESSED_DATA_DIR / "amazon"
API_PROCESSED_DIR = PROCESSED_DATA_DIR / "api"

#Logs
LOG_DIR = PROJECT_ROOT / "logs"

#API
FAKESTORE_API = "https://fakestoreapi.com/products"