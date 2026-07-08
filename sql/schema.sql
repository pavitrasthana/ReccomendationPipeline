CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    asin TEXT,
    name TEXT,
    brand TEXT,
    category TEXT,
    price FLOAT
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    product_id TEXT REFERENCES products(product_id),
    username TEXT,
    rating FLOAT,
    review_date TIMESTAMP,
    review_title TEXT,
    review_text TEXT
);

CREATE TABLE api_products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT,
    price FLOAT,
    description TEXT,
    image TEXT
);