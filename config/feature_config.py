"""
Feature engineering configuration for Amazon Reviews dataset.
"""

# =====================================================
# Text Columns
# =====================================================

TEXT_COLUMNS = [
    "reviews.text",
    "reviews.title"
]

# =====================================================
# User & Product Columns
# =====================================================

USER_COLUMN = "reviews.username"

PRODUCT_COLUMN = "name"

RATING_COLUMN = "reviews.rating"

# =====================================================
# Feature Flags
# =====================================================

CREATE_TEXT_LENGTH = True

CREATE_WORD_COUNT = True

CREATE_USER_FEATURES = True

CREATE_PRODUCT_FEATURES = True