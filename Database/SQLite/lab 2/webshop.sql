BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "books" (
	"book_id"	INTEGER,
	"title"	TEXT NOT NULL,
	"author"	TEXT,
	"year"	INTEGER CHECK("year" > 1400),
	PRIMARY KEY("book_id")
);
CREATE TABLE IF NOT EXISTS "customers" (
	"customer_id"	INTEGER,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT UNIQUE,
	"city"	TEXT,
	"joined_date"	TEXT,
	PRIMARY KEY("customer_id")
);
CREATE TABLE IF NOT EXISTS "order_items" (
	"order_id"	INTEGER NOT NULL,
	"product_id"	INTEGER NOT NULL,
	"quantity"	INTEGER NOT NULL CHECK("quantity" > 0),
	"unit_price"	REAL NOT NULL,
	PRIMARY KEY("order_id","product_id"),
	FOREIGN KEY("order_id") REFERENCES "orders"("order_id"),
	FOREIGN KEY("product_id") REFERENCES "products"("product_id")
);
CREATE TABLE IF NOT EXISTS "orders" (
	"order_id"	INTEGER,
	"customer_id"	INTEGER NOT NULL,
	"order_date"	TEXT NOT NULL,
	"status"	TEXT NOT NULL DEFAULT 'new' CHECK("status" IN ('new', 'shipped', 'delivered', 'cancelled')),
	PRIMARY KEY("order_id"),
	FOREIGN KEY("customer_id") REFERENCES "customers"("customer_id")
);
CREATE TABLE IF NOT EXISTS "products" (
	"product_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"category"	TEXT,
	"price"	REAL,
	"stock"	INTEGER,
	PRIMARY KEY("product_id")
);
CREATE TABLE IF NOT EXISTS "reviews" (
	"review_id"	INTEGER,
	"product_id"	INTEGER,
	"rating"	INTEGER CHECK("rating" BETWEEN 1 AND 5),
	"comment"	TEXT,
	PRIMARY KEY("review_id"),
	FOREIGN KEY("product_id") REFERENCES "products"("product_id")
);
COMMIT;
