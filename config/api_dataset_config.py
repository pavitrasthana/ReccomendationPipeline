"""
Dataset configuration for FakeStore API.
"""

# =====================================================
# Dataset Information
# =====================================================

DATASET_NAME = "FakeStore API"

# =====================================================
# Primary Key
# =====================================================

PRIMARY_KEY = "id"

# =====================================================
# Required Columns
# =====================================================

REQUIRED_COLUMNS = [
    "id",
    "title",
    "price",
    "description",
    "category",
    "image",
    "rating.rate",
    "rating.count"
]

# =====================================================
# Expected Data Types
# =====================================================

EXPECTED_DTYPES = {
    "id": "int64",
    "title": "object",
    "price": "float64",
    "description": "object",
    "category": "object",
    "image": "object",
    "rating.rate": "float64",
    "rating.count": "int64"
}

# =====================================================
# Validation Columns
# =====================================================

PRICE_COLUMN = "price"

RATING_COLUMN = "rating.rate"