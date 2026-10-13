import sqlite3


def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("That is not a number")
        return

    conn.execute(
                "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
                (name, category, price, stock))
    conn.commit()
    print("Saved!")


def update_product_stock(conn):
    product_id = int(input("Product ID : "))
    stock = int(input("Stock : "))
    cursor = conn.execute(
                "UPDATE products SET stock = ? WHERE product_id = ?",
                (stock, product_id))
    conn.commit()
    if cursor.rowcount == 1:
        print("Updated!")
    else:
        print("No product with that id")


def order_receipt(conn):
    order_id = int(input("Order ID : "))
    cursor = conn.execute("""
            SELECT products.name, order_items.quantity, order_items.unit_price
            FROM products
            INNER JOIN order_items ON order_items.product_id = products.product_id
            WHERE order_items.order_id = ?
            """, (order_id,))
    rows = cursor.fetchall()
    if not rows:
        print("No products found.")
    for name, quantity, unit_price in rows:
        print(f"{name:<20}  {quantity:>5} {unit_price:>8.2f}")


def top_selling_products(conn):
    cursor = conn.execute("""
                SELECT products.name, SUM(order_items.quantity) AS total_items
                FROM products
                INNER JOIN order_items
                ON products.product_id = order_items.product_id
                GROUP BY order_items.product_id
                ORDER BY total_items DESC, products.name
                LIMIT 3
                """)
    rows = cursor.fetchall()
    for position, item in enumerate(rows, start=1):
        print(f" {position}. {item[0]} ({item[1]})")


def main():
    conn = connect()
    while True:
        print("\n" \
        "1) List products  " \
        "2) Search customers  " \
        "3) Add product  " \
        "4) Change Stock  " \
        "5) Order's receipt  " \
        "6) Top 3 best-selling products  " \
        "0) Quit  ")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            update_product_stock(conn)
        elif choice == "5":
            order_receipt(conn)
        elif choice == "6":
            top_selling_products(conn)
        elif choice == "0":
            break
    conn.close()


main()

# Exercise 5
# Add a menu option 4 to shop.py: change the stock of a product.
# Ask for the product id and the new stock.
# Created update_product_stock() function and added menu option 4

# Exercise 6
# Add a menu option 5 to shop.py: show an order's receipt.
# Ask for the order_id and use a JOIN to show product names.
# Created order_receipt() function and added menu option 5

# Exercise 7
# What happens in add_product if the user types abc as the price?
# Fix it with try/except.
#
# Before the fix, the program crashed with:
#   ValueError: could not convert string to float: 'abc'
# float() cannot turn the text "abc" into a number. Nothing handled the error,
# so the whole program stopped and the menu was gone. No product was saved.
#
# I fixed it by putting the price and stock inputs inside a try block.
# If the user types something that is not a number, the except ValueError
# block prints a message and returns, so the INSERT never runs and the
# program goes back to the menu.

# Exercise 8
# Challenge: add a menu option 6, 'top 3 best-selling products'.
# Use GROUP BY, ORDER BY and LIMIT.
# Expected: 3 lines
