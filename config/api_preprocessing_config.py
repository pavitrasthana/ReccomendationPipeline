"""
Preprocessing configuration for FakeStore API dataset.
"""

# =====================================================
# Missing Value Handling
# =====================================================

DROP_ROWS_WITH_MISSING = [
    "price"
]

FILL_MISSING_VALUES = {}

# =====================================================
# Duplicate Handling
# =====================================================

REMOVE_DUPLICATES = True

# =====================================================
# Columns to Drop
# =====================================================

DROP_COLUMNS = []

# =====================================================
# Text Processing
# =====================================================

TEXT_COLUMNS = [
    "title",
    "description",
    "category"
]

LOWERCASE_TEXT = True
#REMOVE_EXTRA_WHITESPACE = True
CONVERT_TO_LOWERCASE = True
REMOVE_EXTRA_WHITESPACE = True

# =====================================================
# Date Columns
# =====================================================

DATE_COLUMNS = []