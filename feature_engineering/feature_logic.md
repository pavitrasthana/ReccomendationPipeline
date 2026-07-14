# Feature Engineering Summary

This document describes the engineered features created for the Recommendation Pipeline.

---

# Amazon Reviews Dataset

## reviews.text_length

Number of characters in the review text.

Purpose:
Captures review verbosity.

---

## reviews.text_word_count

Number of words in the review text.

Purpose:
Measures review richness.

---

## reviews.title_length

Number of characters in the review title.

Purpose:
Provides an additional text-based feature.

---

## reviews.title_word_count

Number of words in the review title.

Purpose:
Captures title complexity.

---

## user_review_count

Total number of reviews written by a user.

Purpose:
Represents user activity frequency.

---

## user_average_rating

Average rating given by a user.

Purpose:
Represents user rating behaviour.

---

## product_review_count

Total number of reviews received by a product.

Purpose:
Measures product popularity.

---

## product_average_rating

Average rating received by a product.

Purpose:
Represents overall product quality.

---

## product_unique_user_count

Number of unique users who reviewed a product.

Purpose:
Simple collaborative-filtering (co-occurrence) feature suitable for recommendation algorithms.

------------------------------------------------------------

# FakeStore API Dataset

## title_length

Number of characters in the product title.

Purpose:
Captures title richness.

---

## title_word_count

Number of words in the title.

Purpose:
Measures title complexity.

---

## description_length

Number of characters in the description.

Purpose:
Captures product description richness.

---

## description_word_count

Number of words in the description.

Purpose:
Measures product description complexity.

---

## price_bucket

Categorizes products into:

- Low
- Medium
- High

Purpose:
Useful for price-based recommendations.

---

## product_popularity

Derived from rating.count.

Purpose:
Represents product popularity.