# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:32:52 2026

@author: pavit
"""

import json

from utils.file_utils import ensure_directory
from utils.constants import VALIDATION_REPORT_DIR
from utils.time_utils import get_timestamp

class QualityReportGenerator:
    """
    Generates validation reports.
    """
    @staticmethod
    def generate(profile_report, validation_summary):
        ensure_directory(VALIDATION_REPORT_DIR)
        report = {
            "report_timestamp": get_timestamp(),
            "dataset_profile": profile_report.to_dict(),
            "validation_summary": validation_summary.to_dict(),
        }
        filename = (
            VALIDATION_REPORT_DIR /
            f"validation_{get_timestamp()}.json"
        )
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                report,
                file,
                indent=4
            )
        return filename