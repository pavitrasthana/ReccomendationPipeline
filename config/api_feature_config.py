"""
Feature engineering configuration for FakeStore API.
"""

# =====================================================
# Text Columns
# =====================================================

TEXT_COLUMNS = [
    "title",
    "description"
]

# =====================================================
# Product Columns
# =====================================================

PRICE_COLUMN = "price"

CATEGORY_COLUMN = "category"

RATING_COLUMN = "rating.rate"

POPULARITY_COLUMN = "rating.count"

# =====================================================
# Feature Flags
# =====================================================

CREATE_TEXT_LENGTH = True

CREATE_WORD_COUNT = True

CREATE_PRICE_BUCKET = True

CREATE_POPULARITY_FEATURE = True