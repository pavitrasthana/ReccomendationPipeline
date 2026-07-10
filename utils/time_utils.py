# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:47:44 2026

@author: pavit
"""
import uuid

from datetime import datetime

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def generate_run_id():
    return str(uuid.uuid4())