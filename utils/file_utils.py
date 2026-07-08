# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:09:35 2026

@author: pavit
"""

from pathlib import Path

def ensure_directory(path:Path):
    #Create directory if does not exists
    path.mkdir(parents=True,exist_ok=True)
    