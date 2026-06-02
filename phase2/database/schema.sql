
CREATE TABLE products(
 id SERIAL PRIMARY KEY,
 name VARCHAR(255),
 price NUMERIC(10,2)
);

CREATE TABLE inventory(
 id SERIAL PRIMARY KEY,
 product_id INT,
 quantity INT
);

CREATE TABLE orders(
 id SERIAL PRIMARY KEY,
 customer_name VARCHAR(255),
 total NUMERIC(10,2)
);

CREATE TABLE order_items(
 id SERIAL PRIMARY KEY,
 order_id INT,
 product_id INT,
 quantity INT,
 price NUMERIC(10,2)
);

create table users(
 id SERIAL PRIMARY KEY,
 username VARCHAR(255) UNIQUE,
 password VARCHAR(255)
);
