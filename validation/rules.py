# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:28:18 2026

@author: pavit
"""

import pandas as pd
from config.dataset_config import REQUIRED_COLUMNS
from models.validation_result import ValidationResult
from config.dataset_config import *
from config.validation_config import *

class ValidationRules:
    #Check duplicates
    @staticmethod
    def check_duplicates(df:pd.DataFrame):
        duplicate_count = int(df.duplicated().sum())
        if duplicate_count <= MAX_DUPLICATES:
            return ValidationResult(
                rule="Duplicate Check",
                status=PASS,
                severity=INFO,
                message="No duplicate rows found",
                details={
                    "duplicated_count": duplicate_count
                    }
                )
        return ValidationResult(
            rule="Duplicate Check",
            status=FAIL,
            severity=ERROR,
            message=f"{duplicate_count} duplicate rows found.",
            details={
                "duplicate_count": duplicate_count
                }
            )
    
    #MissingRequiredColumns
    @staticmethod
    def check_required_columns(df):
        missing =[
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
    
    #Check Missing Values
    @staticmethod
    def check_missing_values(df):
        missing ={}
        for column in REQUIRED_COLUMNS:
            count = int(df[column].isnull().sum())
            if count>0:
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
            severity=WARNING,
            message="Missing values detected.",
            details=missing
        )
    
    @staticmethod
    def check_rating_range(df):
        rating = df[RATING_COLUMN]
        invalid = (
            rating.dropna()
            .between(
                RATING_MIN,
                RATING_MAX
            )
            == False
        ).sum()
        if invalid == 0:
            return ValidationResult(
                rule="Rating Range",
                status=PASS,
                severity=INFO,
                message="Ratings within range.",
                details={}
            )
        return ValidationResult(
            rule="Rating Range",
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

                message="All data types valid.",

                details={}

            )

        return ValidationResult(

            rule="Data Types",

            status=WARNING,

            severity=WARNING,

            message="Unexpected data types.",

            details=mismatches

        )    
    
    