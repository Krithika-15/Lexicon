-- LAB 2

-- 1. Create a table books with: book_id (primary key), title (must have a value), author, year (whole number).
CREATE TABLE books(
book_id	INTEGER PRIMARY KEY,
title	TEXT NOT NULL,
author	TEXT,
year	INTEGER
);

-- 2. Add a rule to books so year must be greater than 1400. (Hint: DROP and CREATE again.)
DROP TABLE books;
CREATE TABLE books(
book_id	INTEGER PRIMARY KEY,
title	TEXT NOT NULL,
author	TEXT,
year	INTEGER CHECK (year > 1400)
);

-- 3. Add a column isbn to books. It should be TEXT.
ALTER TABLE books ADD COLUMN isbn TEXT;

-- 4. Delete the books table.
DROP TABLE books;

-- 5. Create a table reviews: review_id, product_id (points to products), rating (1 to 5), comment.
CREATE TABLE reviews(
review_id	INTEGER PRIMARY KEY,
product_id	INTEGER,
rating		INTEGER CHECK (rating BETWEEN 1 and 5),
comment		TEXT,
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 6. Test reviews: try to add a review with rating 6. What happens?
INSERT INTO reviews(product_id, rating, comment) VALUES(2, 6, 'good');
-- Error CHECK constraint failed: rating BETWEEN 1 and 5

-- 7. Test reviews: try to add a review for product 50. What happens?
INSERT INTO reviews(product_id, rating, comment) VALUES(50, 3, 'average');
-- Error Result: FOREIGN KEY constraint failed

-- 8. On paper: draw the 4 webshop tables as boxes and draw arrows for each foreign key.
CREATE TABLE orders(
	order_id	INTEGER PRIMARY KEY,
	customer_id	INTEGER NOT NULL,
	order_date	TEXT NOT NULL,
	status		TEXT NOT NULL DEFAULT 'new'
		CHECK (status IN ('new', 'shipped', 'delivered', 'cancelled')),
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items(
	order_id 	INTEGER NOT NULL,
	product_id	INTEGER NOT NULL,
	quantity	INTEGER NOT NULL CHECK (quantity > 0),
	unit_price	REAL NOT NULL,
	PRIMARY KEY (order_id, product_id),
	FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);
