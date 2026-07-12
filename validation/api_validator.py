"""
Validation engine for FakeStore API.
"""

import pandas as pd

from validation.api_rules import APIValidationRules

from models.validation_summary import ValidationSummary

from config.api_validation_config import (
    PASS,
    WARNING,
    FAIL
)


class APIDataValidator:
    """
    Executes all validation rules for the
    FakeStore API dataset.
    """

    def validate(self, df: pd.DataFrame) -> ValidationSummary:

        results = [

            APIValidationRules.check_duplicates(df),

            APIValidationRules.check_required_columns(df),

            APIValidationRules.check_missing_values(df),

            APIValidationRules.check_price(df),

            APIValidationRules.check_rating(df),

            APIValidationRules.check_data_types(df)

        ]

        passed = sum(
            r.status == PASS
            for r in results
        )

        warnings = sum(
            r.status == WARNING
            for r in results
        )

        failed = sum(
            r.status == FAIL
            for r in results
        )

        if failed:

            overall = FAIL

        elif warnings:

            overall = WARNING

        else:

            overall = PASS

        return ValidationSummary(

            overall_status=overall,

            total_rules=len(results),

            passed_rules=passed,

            warning_rules=warnings,

            failed_rules=failed,

            results=results

        )