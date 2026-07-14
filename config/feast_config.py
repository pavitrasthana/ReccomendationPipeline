"""
Feast Feature Store configuration.
"""

from pathlib import Path

from utils.constants import PROJECT_ROOT

# =====================================================
# Feast Project
# =====================================================

FEAST_PROJECT_NAME = "recommendation_pipeline"

# =====================================================
# Feast Repository
# =====================================================

FEATURE_STORE_DIR = (
    PROJECT_ROOT /
    "feature_store"
)

FEATURE_STORE_CONFIG = (
    FEATURE_STORE_DIR /
    "feature_store.yaml"
)

# =====================================================
# Registry
# =====================================================

REGISTRY_PATH = (
    FEATURE_STORE_DIR /
    "registry.db"
)

# =====================================================
# Offline Store
# =====================================================

OFFLINE_STORE_TYPE = "postgres"

# =====================================================
# Online Store
# =====================================================

ONLINE_STORE_TYPE = "sqlite"

ONLINE_STORE_PATH = (
    FEATURE_STORE_DIR /
    "online_store.db"
)