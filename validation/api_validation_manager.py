"""
Validation manager for FakeStore API.
"""

import json
import pandas as pd

from utils.api_utils import get_latest_api_file
from utils.constants import RAW_API_DIR

from validation.profiler import DataProfiler
from validation.api_validator import APIDataValidator
from validation.api_ge_validator import APIGEValidator
from validation.quality_report import QualityReportGenerator


class APIValidationManager:

    def run(self):

        latest_file = get_latest_api_file(
            RAW_API_DIR
        )

        with open(latest_file, "r", encoding="utf-8") as file:

            products = json.load(file)

        df = pd.json_normalize(products)

        profile = DataProfiler.profile(df)

        validator = APIDataValidator()

        summary = validator.validate(df)

        ge_result = APIGEValidator.validate(df)

        report = QualityReportGenerator.generate(
            profile,
            summary,
            ge_result
        )

        print(f"API validation report generated:\n{report}")

        return profile, summary
    
if __name__ == "__main__":

    manager = APIValidationManager()

    manager.run()