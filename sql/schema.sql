-- =====================================================
-- Amazon Processed Reviews
-- =====================================================

DROP TABLE IF EXISTS amazon_reviews CASCADE;

CREATE TABLE amazon_reviews (

    id TEXT,
    asins TEXT,
    brand TEXT,
    categories TEXT,
    colors TEXT,
    dateadded TIMESTAMP,
    dateupdated TIMESTAMP,
    dimension TEXT,
    ean DOUBLE PRECISION,
    keys TEXT,
    manufacturer TEXT,
    manufacturernumber TEXT,
    name TEXT,
    prices TEXT,
    reviews_date TIMESTAMP,
    reviews_dorecommend BOOLEAN,
    reviews_numhelpful DOUBLE PRECISION,
    reviews_rating DOUBLE PRECISION,
    reviews_sourceurls TEXT,
    reviews_text TEXT,
    reviews_title TEXT,
    reviews_username TEXT,
    upc DOUBLE PRECISION,
    weight TEXT

);

-- =====================================================
-- Amazon Engineered Features
-- =====================================================

DROP TABLE IF EXISTS amazon_features CASCADE;

CREATE TABLE amazon_features (

    id TEXT,
    asins TEXT,
    brand TEXT,
    categories TEXT,
    colors TEXT,
    dateadded TIMESTAMP,
    dateupdated TIMESTAMP,
    dimension TEXT,
    ean DOUBLE PRECISION,
    keys TEXT,
    manufacturer TEXT,
    manufacturernumber TEXT,
    name TEXT,
    prices TEXT,
    reviews_date TIMESTAMP,
    reviews_dorecommend BOOLEAN,
    reviews_numhelpful DOUBLE PRECISION,
    reviews_rating DOUBLE PRECISION,
    reviews_sourceurls TEXT,
    reviews_text TEXT,
    reviews_title TEXT,
    reviews_username TEXT,
    upc DOUBLE PRECISION,
    weight TEXT,

    reviews_text_length INTEGER,
    reviews_text_word_count INTEGER,
    reviews_title_length INTEGER,
    reviews_title_word_count INTEGER,
    user_review_count INTEGER,
    user_average_rating DOUBLE PRECISION,
    product_review_count INTEGER,
    product_average_rating DOUBLE PRECISION,
    product_unique_user_count INTEGER

);

-- =====================================================
-- API Processed Products
-- =====================================================

DROP TABLE IF EXISTS api_products CASCADE;

CREATE TABLE api_products (

    id INTEGER PRIMARY KEY,
    title TEXT,
    price DOUBLE PRECISION,
    description TEXT,
    category TEXT,
    image TEXT,
    rating_rate DOUBLE PRECISION,
    rating_count INTEGER

);

-- =====================================================
-- API Engineered Features
-- =====================================================

DROP TABLE IF EXISTS api_product_features CASCADE;

CREATE TABLE api_product_features (

    id INTEGER PRIMARY KEY,
    title TEXT,
    price DOUBLE PRECISION,
    description TEXT,
    category TEXT,
    image TEXT,
    rating_rate DOUBLE PRECISION,
    rating_count INTEGER,

    title_length INTEGER,
    title_word_count INTEGER,
    description_length INTEGER,
    description_word_count INTEGER,
    price_bucket TEXT,
    product_popularity INTEGER

);