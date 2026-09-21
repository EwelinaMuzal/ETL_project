CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    country TEXT,
    city TEXT,
    registration_date TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT,
    customer_id TEXT,
    order_date TEXT,
    status TEXT,
    currency TEXT
);