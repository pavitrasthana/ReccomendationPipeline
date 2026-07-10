# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:34:03 2026

@author: pavit
"""

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class ProfileReport:

    rows: int
    columns: int

    memory_usage_mb: float

    duplicate_count: int
    duplicate_percentage: float

    missing_values: Dict[str, int]
    missing_percentage: Dict[str, float]

    unique_values: Dict[str, int]

    data_types: Dict[str, str]

    column_names: List[str]

    def to_dict(self):

        return asdict(self)