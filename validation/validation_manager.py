# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:40:05 2026

@author: pavit
"""

import pandas as pd

from utils.constants import RAW_AMAZON_DIR

from validation.profiler import DataProfiler
from validation.validator import DataValidator
from validation.quality_report import QualityReportGenerator
from validation.ge_validator import GEValidator


class ValidationManager:
    def run(self):
        df = pd.read_csv(
            RAW_AMAZON_DIR / "amazon_reviews.csv"
        )
        profile = DataProfiler.profile(df)
        validator = DataValidator()
        summary = validator.validate(df)
        ge_result =  GEValidator.validate(df)
        report = QualityReportGenerator.generate(
            profile,
            summary,
            ge_result
        )
        print(f"Validation report generated:\n{report}")
        return profile, summary
    
if __name__ == "__main__":
    manager = ValidationManager()
    manager.run()