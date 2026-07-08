# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:11:29 2026

@author: pavit
"""

import time
from functools import wraps
from config.logger import logger

def retry(max_attempts=3 , delay =2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, max_attempts + 1):

                try:

                    return func(*args, **kwargs)

                except Exception as e:

                    logger.warning(
                        f"Attempt {attempt} failed : {e}"
                    )

                    if attempt == max_attempts:
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator