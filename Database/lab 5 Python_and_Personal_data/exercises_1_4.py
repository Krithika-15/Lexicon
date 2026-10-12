# Exercise 1
# Write a script that prints all customers as 'First Last (City)'.
# Expected: 10 lines
import sqlite3

conn = sqlite3.connect("webshop.db")
cur = conn.cursor()

cur.execute("SELECT first_name, last_name, city FROM customers")
rows = cur.fetchall()

for row in rows:
    print(f"{row[0]} {row[1]} ({row[2]})")



# Exercise 2
# Ask the user for a max price and show all products cheaper than that.
# Use a ? placeholder.
max_price = float(input("Enter the maximum price : "))
cur.execute("SELECT name, category, price, stock FROM products WHERE price < ?", (max_price,))
rows = cur.fetchall()

if not rows:
    print(f"There is no product cheaper than {max_price:.2f}")
else:
    print(f"{'Name':<18}{'Category':<15}{'Price':>10}{'Stock':>12}")
    print("-------------------------------------------------------")
    for row in rows:
        print(f"{row[0]:<18}{row[1]:<15}{row[2]:>10.2f}{row[3]:>12}")



# Exercise 3
# Ask the user for a category and print how many products it has.
# Use COUNT and fetchone().
category = (input("Enter the product category : ")).lower()
cur.execute("SELECT COUNT(*) FROM products WHERE LOWER(category) = ?", (category,))
result = cur.fetchone()
print(f"Category {category} has {result[0]} products")

conn.close()



# Exercise 4
# Explain in your own words: why is building SQL with an f-string dangerous,
# and why is a ? placeholder safe?
# Expected: a few sentences
# Unsafe demo, do not use:
# category = input("Enter category (unsafe version): ")
# query = f"SELECT COUNT(*) FROM products WHERE category = '{category}'"
# print(query)
# cur.execute(query)
# print(cur.fetchone()[0])
#
# With an f-string, whatever the user types is pasted straight into the SQL text.
# So if the user types SQL instead of a normal value, the database runs it as
# part of the query. This is called SQL injection.
# SQL injection is a code injection technique that can destroy your database.
# SQL injections are a common web hacking technique.
# I tested it: I typed  x' OR '1'='1  as the category. With the f-string the
# query became  WHERE category = 'x' OR '1'='1'  which is true for every row,
# so I got 12 (all products) instead of 0.

# With a ? placeholder, the query and the value are sent to the database
# separately. The input is only ever treated as a value, never as SQL.
# The same input gave 0, because no category has that name.


# notes :
# conn = sqlite3.connect("webshop.db") => Open Database
# cur = conn.cursor() => Click on the Execute SQL tab (empty, nothing typed)
# cur.execute("SELECT ...")	=> Type the query and press ▶
# rows = cur.fetchall() => Look at the result grid
# conn.close() => Close Database used at the end as using the same connection for all exercises

# cur.execute("SELECT * FROM products WHERE price < ?", (max_price,))
# execute always needs a container, just (max_price) is int not a tuple
# It is the comma that creates a tuple, not the brackets.

# fetchall() → list of tuples
# fetchone() → one tuple, like (3,)
# fetchone() gives a tuple even though there is only one number in it,
# because a row is always a tuple. That is why you need [0] to take the number out.
