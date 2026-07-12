"""
Validation rules for FakeStore API.
"""

import pandas as pd

from models.validation_result import ValidationResult

from config.api_dataset_config import (
    REQUIRED_COLUMNS,
    EXPECTED_DTYPES,
    PRIMARY_KEY,
    PRICE_COLUMN,
    RATING_COLUMN
)

from config.api_validation_config import (
    MAX_DUPLICATES,
    DEFAULT_MISSING_THRESHOLD,
    PRICE_MIN,
    RATING_MIN,
    RATING_MAX,
    PASS,
    WARNING,
    FAIL,
    INFO,
    WARNING_SEVERITY,
    ERROR
)

class APIValidationRules:
    """
    Validation rules for FakeStore API dataset.
    """
    
    @staticmethod
    def check_duplicates(df: pd.DataFrame):
    
        duplicate_count = int(df.duplicated(subset=[PRIMARY_KEY]).sum())
    
        if duplicate_count <= MAX_DUPLICATES:
    
            return ValidationResult(
                rule="Duplicate Product IDs",
                status=PASS,
                severity=INFO,
                message="No duplicate product IDs found.",
                details={
                    "duplicate_count": duplicate_count
                }
            )
    
        return ValidationResult(
            rule="Duplicate Product IDs",
            status=FAIL,
            severity=ERROR,
            message=f"{duplicate_count} duplicate product IDs found.",
            details={
                "duplicate_count": duplicate_count
            }
        )
    
    @staticmethod
    def check_required_columns(df):
    
        missing = [
            column
            for column in REQUIRED_COLUMNS
            if column not in df.columns
        ]
    
        if not missing:
    
            return ValidationResult(
                rule="Required Columns",
                status=PASS,
                severity=INFO,
                message="All required columns exist.",
                details={}
            )
    
        return ValidationResult(
            rule="Required Columns",
            status=FAIL,
            severity=ERROR,
            message="Required columns missing.",
            details={
                "missing_columns": missing
            }
        )
    
    @staticmethod
    def check_missing_values(df):
    
        missing = {}
    
        for column in REQUIRED_COLUMNS:
    
            if column not in df.columns:
                continue
    
            count = int(df[column].isnull().sum())
    
            if count > DEFAULT_MISSING_THRESHOLD:
                missing[column] = count
    
        if not missing:
    
            return ValidationResult(
                rule="Missing Values",
                status=PASS,
                severity=INFO,
                message="No missing values found.",
                details={}
            )
    
        return ValidationResult(
            rule="Missing Values",
            status=WARNING,
            severity=WARNING_SEVERITY,
            message="Missing values detected.",
            details=missing
        )
    
    @staticmethod
    def check_price(df):
    
        invalid = (df[PRICE_COLUMN] < PRICE_MIN).sum()
    
        if invalid == 0:
    
            return ValidationResult(
                rule="Price Validation",
                status=PASS,
                severity=INFO,
                message="All prices are valid.",
                details={}
            )
    
        return ValidationResult(
            rule="Price Validation",
            status=FAIL,
            severity=ERROR,
            message="Negative prices detected.",
            details={
                "invalid_prices": int(invalid)
            }
        )
    
    @staticmethod
    def check_rating(df):
    
        invalid = (
            df[RATING_COLUMN]
            .between(RATING_MIN, RATING_MAX)
            == False
        ).sum()
    
        if invalid == 0:
    
            return ValidationResult(
                rule="Rating Validation",
                status=PASS,
                severity=INFO,
                message="Ratings are within range.",
                details={}
            )
    
        return ValidationResult(
            rule="Rating Validation",
            status=FAIL,
            severity=ERROR,
            message="Invalid ratings detected.",
            details={
                "invalid_ratings": int(invalid)
            }
        )
    
    @staticmethod
    def check_data_types(df):
    
        mismatches = {}
    
        for column, expected in EXPECTED_DTYPES.items():
    
            if column not in df.columns:
                continue
    
            actual = str(df[column].dtype)
    
            if actual != expected:
    
                mismatches[column] = {
                    "expected": expected,
                    "actual": actual
                }
    
        if not mismatches:
    
            return ValidationResult(
                rule="Data Types",
                status=PASS,
                severity=INFO,
                message="All data types are valid.",
                details={}
            )
    
        return ValidationResult(
            rule="Data Types",
            status=WARNING,
            severity=WARNING_SEVERITY,
            message="Unexpected data types.",
            details=mismatches
        )