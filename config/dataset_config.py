"""
Dataset specific configuration.

Changing the dataset should ideally only require
updating this file.
"""

# =====================================================
# Dataset
# =====================================================

DATASET_NAME = "Amazon Product Reviews"

# =====================================================
# Primary Key
# =====================================================

PRIMARY_KEY = "id"

# =====================================================
# Recommendation Target
# =====================================================

RATING_COLUMN = "reviews.rating"

RATING_MIN = 1

RATING_MAX = 5

# =====================================================
# Required Columns
# =====================================================

REQUIRED_COLUMNS = [

    "id",

    "name",

    "brand",

    "categories",

    "prices",

    "reviews.rating",

    "reviews.username",

    "reviews.text"

]

# =====================================================
# Optional Columns
# =====================================================

OPTIONAL_COLUMNS = [

    "reviews.userCity",

    "reviews.userProvince",

    "sizes",

    "colors",

    "dimension",

    "manufacturer",

    "manufacturerNumber",

    "weight"

]

# =====================================================
# Expected Data Types
# =====================================================

EXPECTED_DTYPES = {

    "id": "object",

    "name": "object",

    "brand": "object",

    "categories": "object",

    "prices": "object",

    "reviews.rating": "float64",

    "reviews.username": "object",

    "reviews.text": "object"

}