-- ============================================
-- PART 1: Adding, changing and deleting data
-- Use webshop.db. Check first: SELECT COUNT(*) FROM orders; should give 15.
-- If not, run webshop_reset.sql and press Ctrl+S.
-- ============================================

-- Exercise 1
-- Add yourself as customer number 11 (use a made-up email).
INSERT INTO customers(first_name, last_name, email, city, joined_date) VALUES('Harry', 'Potter', 'harry@mail.com', 'Stockholm', '2025-01-02');

-- Exercise 2
-- Add two new products in one INSERT: Scarf (Accessories, 229 kr, 15 in stock)
-- and Gloves (Accessories, 199 kr, 20 in stock).
INSERT INTO products(name, category, price, stock) VALUES('Scarf', 'Accessories', 229, 15), ('Gloves', 'Accessories', 199, 20);

-- Exercise 3
-- Customer 7 (Emma) orders 2 Beanies (product 10, 179 kr).
-- Make the order (order 16) and the order item.
INSERT INTO orders(customer_id, order_date) VALUES(7, '2026-10-07');
INSERT INTO order_items(order_id, product_id, quantity, unit_price) VALUES(16, 10, 2, 179);


-- Exercise 4
-- Try to add an order item with quantity 0. Which rule stops you?
INSERT INTO order_items(order_id, product_id, quantity, unit_price) VALUES(1, 1, 0, 100.0);
-- Error: CHECK constraint failed: quantity > 0
-- The CHECK rule on order_items.quantity only allows values above 0.

-- Exercise 5
-- Order 12 has been shipped. Change its status.
UPDATE orders SET status = 'shipped' WHERE order_id = 12;

-- Exercise 6
-- The Water Bottle (product 5) is back in stock: 50 pieces.
UPDATE products SET stock = 50 WHERE product_id = 5;

-- Exercise 7
-- Raise the price of all Accessories by 10%.
UPDATE products SET price = price * 1.10 WHERE category = 'Accessories';
SELECT name, price FROM products WHERE category = 'Accessories';

-- Exercise 8
-- Delete the cancelled order. Watch out: its items must go first! Why?
DELETE FROM order_items WHERE order_id = 7;
DELETE FROM orders WHERE status = 'cancelled';
-- Why the items go first:
-- order_items.order_id is a FOREIGN KEY that points to orders.order_id.
-- Every order item must belong to an order that really exists.
-- If I delete order 7 first, its items would point to an order that is gone
-- (these are called "orphan rows"), so the database refuses with:
-- Error: FOREIGN KEY constraint failed
-- So the order is: delete the child rows (order_items) first,
-- then the parent row (orders).

-- Exercise 9
-- Finally: click Revert Changes so your data matches the teacher's again.
-- Check: 15 orders?
SELECT COUNT(*) FROM orders;

-- ============================================
-- PART 2: Designing a good database
-- Exercises 10 to 15 are done on paper or in a drawing tool (no database needed).
-- Exercise 16 is the only one with SQL, and it uses a new file music.db, not webshop.db.
-- ============================================

-- Exercise 10
-- Look at this table: student | phone_numbers | course1 | course2 | course3.
-- List every problem you can find.
-- Problems :
-- 1. phone_numbers holds many values in one cell, e.g. '070-111, 073-222'.
-- One cell should hold one value. This breaks first normal form (1NF).
-- It is hard to search for one number or to change just one of them.
-- 2. course1, course2, course3 are "repeating group"
-- same kind of data spread overal several columns. This also breaks 1NF.
-- A student with more than 3 courses does not fit without adding a new column.
-- Also a student with 1 course leaves two cells empty (NULL).
-- To find everyone who takes a particular course (for example: SQL),
-- then I must check all three columns.
-- 3. No Primary key.
-- Two students with same name, then I cannot point to exact row.
-- 4. Course names are typed again in every row.
-- Incase of typo like 'pyhton' will make it look like a different course.
-- Fix : Need to split it into separate tables.

-- Exercise 11
-- In order_sheet, which normal form does the products column break?
-- How would you fix it?
-- It breaks first normal form (1NF): one value per cell, no lists.
-- Example from the slide: products = 'Hoodie, Cap x2'
-- That single cell holds two products and a quantity as plain text.
-- I cannot easily find every order that contains a Cap.
-- I cannot add up how many Caps were sold: 'x2' is text, not a number.
-- A typo in a product name goes unnoticed, because nothing checks it.
-- Fix: take the products column out of the order and make a middle table,
-- order_items, with one row per product in an order:
-- order_items(order_id, product_id, quantity)
-- order 1, Hoodie, quantity 1
-- order 1, Cap, quantity 2
-- Product names live once in a products table, and order_items points to
-- them with product_id (a foreign key).

-- Exercise 12
-- A table has: order_id | customer_id | customer_email | order_date.
-- Which column is in the wrong place? Why?
-- customer_email is in the wrong place.
-- This table describes about the order.
-- customer_id : describes the order , who placed it.
-- order_date : describes the order, when it was placed.
-- customer_email : describes the customer.
-- This breaks third Normal Form (3NF).
-- Because same email is repeated on every order the customer makes.
-- If the customer changes email, then I must update many rows.
-- fix : need to remove customer_email from this table and keep it in customers table.


-- Exercise 13
-- Music school (in pairs): 'Students take lessons from teachers. A lesson has a
-- date, time, room and instrument. One teacher can teach many instruments.'
-- Underline the things.
-- students, lessons, teachers, instruments are things

-- Exercise 14
-- Find the relationships in the music school. Which are 1:N and which are N:M?
-- 1:N one teacher gives many lessons
-- 1:N one instrument is taught in many lessons
-- N:M many students and many lessons
-- N:M many teachers and many instruments

-- Exercise 15
-- Draw the ER diagram for the music school.
-- ER diagram is in music.erd.json file

-- Exercise 16
-- Write the CREATE TABLE statements for the music school in a new file music.db.
-- Database: create a new file. Click New Database, name it music.db, and click
-- Cancel in the 'Edit table definition' window. Don't create these tables in webshop.db.
CREATE TABLE teachers(
	teacher_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE students(
	student_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE instruments(
	instrument_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);


CREATE TABLE lessons(
	lesson_id INTEGER PRIMARY KEY,
	teacher_id INTEGER NOT NULL,
	instrument_id INTEGER NOT NULL,
	date TEXT NOT NULL,
	time TEXT NOT NULL,
	room TEXT NOT NULL,
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

CREATE TABLE teacher_instruments(
	teacher_id INTEGER REFERENCES teachers(teacher_id),
	instrument_id INTEGER REFERENCES instruments(instrument_id),
	PRIMARY KEY (teacher_id, instrument_id)
);

CREATE TABLE lesson_students(
	lesson_id INTEGER REFERENCES lessons(lesson_id),
	student_id INTEGER REFERENCES students(student_id),
	PRIMARY KEY (lesson_id, student_id)
);
