# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:55:11 2026

@author: pavit
"""

from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO"
)

logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention=5,
    level="INFO"
)