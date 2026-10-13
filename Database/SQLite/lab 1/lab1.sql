-- LAB 1

-- 1. Show the first name and email of all customers. (10 rows)
SELECT first_name, email FROM customers;

-- 2. Show all products in the Shoes category. (3 rows)
SELECT * FROM products WHERE category = 'Shoes';

-- 3. Which customers live in Uppsala? (3 rows)
SELECT * FROM customers WHERE city = 'Uppsala';

-- 4. Which product costs exactly 199 kr? (1 row)
SELECT * FROM products WHERE price = 199;

-- 5. Show all products sorted by name, A to Z. (12 rows)
SELECT * FROM products ORDER BY name;

-- 6. Show all customers, the one who joined first at the top. (10 rows)
SELECT * FROM customers ORDER BY joined_date;

-- 7. Which products are sold out (stock is 0)? (2 rows)
SELECT * FROM products WHERE stock = 0;

-- 8. Show the 3 newest customers. (3 rows)
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

-- 9. Show customers from Stockholm or Göteborg. Use IN. (4 rows)
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');

-- 10. Show product name and price, but call the columns product and price_sek. (12 rows)
SELECT name AS product, price AS price_sek FROM products;


-- BONUS QUESTIONS

-- B1. Show products that are Clothing or Shoes and cost more than 1000 kr.
--     Hint: you need brackets. Try without them too: why is the answer different? (3 rows)
SELECT * FROM products WHERE category IN ('Clothing', 'Shoes') AND price > 1000;
SELECT * FROM products WHERE (category = 'Clothing' OR category = 'Shoes') AND price > 1000;
-- Without brackets AND runs before OR, so the price check only applies to Shoes (7 rows).


-- B2. For every product in stock, show name, price, stock and the total value
--     of the stock (price x stock) as stock_value. Highest value first. (10 rows)
SELECT name, price, stock, price * stock AS stock_value
FROM products
WHERE stock > 0
ORDER BY stock_value DESC;

-- B3. Which customers have a first name with exactly 4 letters?
--     Hint: _ in LIKE means "exactly one character". (4 rows)
SELECT * FROM customers WHERE first_name LIKE '____';


-- B4. Sort the products by price, cheapest first, and show only products number 6 to 10.
--     Hint: look up OFFSET. (5 rows)
SELECT * FROM products ORDER BY price LIMIT 5 OFFSET 5;
