"""
Application configuration.

Loads environment variables from the project root
regardless of the current working directory.
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# =====================================================
# Project Root
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# =====================================================
# Environment File
# =====================================================

ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


# =====================================================
# PostgreSQL
# =====================================================

POSTGRES_HOST = os.getenv("POSTGRES_HOST")

POSTGRES_PORT = os.getenv("POSTGRES_PORT")

POSTGRES_DB = os.getenv("POSTGRES_DB")

POSTGRES_USER = os.getenv("POSTGRES_USER")

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# =====================================================
# Logging
# =====================================================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)