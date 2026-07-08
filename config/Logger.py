# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:55:11 2026

@author: pavit
"""

from loguru import logger
import sys
from utils.constants import LOG_DIR

logger.remove()

logger.add(
    sys.stdout,
    level="INFO"
)

logger.add(
    LOG_DIR/"app.log",
    rotation="10 MB",
    retention=5,
    level="INFO"
)