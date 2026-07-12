# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:10:23 2026

@author: pavit
"""

import pandas as pd
from validation.rules import ValidationRules
from models.validation_summary import ValidationSummary
from config.validation_config import (
    PASS,
    WARNING,
    FAIL
)

class DataValidator:

    """
    Executes all validation rules.
    """

    def validate(self, df: pd.DataFrame) -> ValidationSummary:
        results = [
            ValidationRules.check_duplicates(df),
            ValidationRules.check_required_columns(df),
            ValidationRules.check_missing_values(df),
            ValidationRules.check_rating_range(df),
            ValidationRules.check_data_types(df)
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