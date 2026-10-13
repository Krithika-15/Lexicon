-- Exercise 9
-- Anna (customer 1) asks: 'Which products have I bought?'
-- Write the query that answers her. Show product names only, each once.
-- Expected: 4 rows
SELECT DISTINCT products.name
FROM products
INNER JOIN order_items
	ON order_items.product_id = products.product_id
INNER JOIN orders
	ON orders.order_id = order_items.order_id
WHERE orders.customer_id = 1;


-- Exercise 10
-- Erik says his email is wrong. Correct it to erik.johansson@example.com.
-- Expected: 1 row changed
SELECT * FROM customers WHERE customer_id = 2;
UPDATE customers SET email = 'erik.johansson@example.com' WHERE customer_id = 2;


-- Exercise 11
-- Create a view customer_overview that a support person can use:
-- customer_id, first name, city and number of orders, but no email.
-- Customers with no orders must also be shown.
-- Expected: 10 rows when you SELECT from the view
CREATE VIEW customer_overview AS
SELECT customers.customer_id, customers.first_name, customers.city, COUNT(orders.order_id) as no_of_orders
FROM customers
LEFT JOIN orders
	ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id;
SELECT * FROM customer_overview;


-- Exercise 12
-- Discuss in pairs: the webshop wants to add a birth_date column 'just in case'.
-- What would you say? Write two sentences.
-- Expected: two sentences
-- I would say no: under GDPR, personal data like birth_date needs a specific purpose (purpose limitation), and 'just in case' is not a purpose.
-- It also adds risk, because a name together with a birth date is useful to a fraudster if the database leaks, so if the shop has a real need such as
-- age-limited products, it should store only what is needed, like the birth year.
