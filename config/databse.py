# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:57:42 2026

@author: pavit
"""

from sqlalchemy import create_engine
from config.config import *

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True
)