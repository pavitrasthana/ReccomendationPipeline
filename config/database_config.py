"""
Database loading configuration.
"""

# =====================================================
# PostgreSQL Tables
# =====================================================

AMAZON_PROCESSED_TABLE = "amazon_reviews"

AMAZON_FEATURE_TABLE = "amazon_features"

API_PROCESSED_TABLE = "products"

API_FEATURE_TABLE = "product_features"

# =====================================================
# Loading Strategy
# =====================================================

IF_EXISTS = "replace"

INDEX = False

CHUNK_SIZE = 1000