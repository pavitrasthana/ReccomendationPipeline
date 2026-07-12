"""
Preprocessing configuration for Amazon Reviews dataset.
"""

# =====================================================
# Missing Value Handling
# =====================================================

DROP_ROWS_WITH_MISSING = [
    "reviews.rating"
]

FILL_MISSING_VALUES = {
    "reviews.username": "Unknown"
}

# =====================================================
# Duplicate Handling
# =====================================================

REMOVE_DUPLICATES = True

# =====================================================
# Columns to Drop
# =====================================================

DROP_COLUMNS = [
    "reviews.userCity",
    "reviews.userProvince",
    "sizes"
]

# =====================================================
# Text Processing
# =====================================================

TEXT_COLUMNS = [
    "reviews.text",
    "reviews.title",
    "reviews.username",
    "brand",
    "name"
]

LOWERCASE_TEXT = True
CONVERT_TO_LOWERCASE=True
REMOVE_EXTRA_WHITESPACE = True

# =====================================================
# Date Columns
# =====================================================

DATE_COLUMNS = [
    "reviews.date",
    "dateAdded",
    "dateUpdated"
]