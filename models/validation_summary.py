# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:06:36 2026

@author: pavit
"""

from dataclasses import dataclass, asdict
from typing import List

from models.validation_result import ValidationResult

@dataclass
class ValidationSummary:
    """
    Represents the complete validation outcome for a dataset.
    """

    overall_status: str

    total_rules: int

    passed_rules: int

    warning_rules: int

    failed_rules: int

    results: List[ValidationResult]

    def to_dict(self):

        return {

            "overall_status": self.overall_status,

            "total_rules": self.total_rules,

            "passed_rules": self.passed_rules,

            "warning_rules": self.warning_rules,

            "failed_rules": self.failed_rules,

            "results": [

                result.to_dict()

                for result in self.results

            ]

        }