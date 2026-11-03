# Database

My database labs. Most of them use the same small webshop database (customers, products, orders and so on). I did the SQL part in SQLite and then a few labs in MongoDB.

## SQLite

| Lab | What it covers |
| --- | --- |
| lab 1 | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `LIKE`, `IN` (plus extra challenges) |
| lab 2 | Creating tables with primary keys, `NOT NULL` and `CHECK` rules |
| lab 3 | `INSERT`, `UPDATE`, `DELETE`, and designing a music school database |
| lab 4 | Joining tables |
| lab 5 | Using SQLite from Python with `sqlite3`, and questions about personal data |

The questions are written as comments in the `.sql` files with my query under each one. Each lab folder has its own copy of `webshop.db`. Labs 3 and 4 also have `webshop_reset.sql` to get the database back to a clean state.

To run a query, open the `webshop.db` from that lab in DB Browser for SQLite, go to Execute SQL, paste the query and press F5.

For lab 5, run the Python files from inside the lab folder so they find `webshop.db`:

    cd "SQLite/lab 5 Python_and_Personal_data"
    python shop.py

## MongoDB

| Lab | What it covers |
| --- | --- |
| lab 1 | `find`, `insert_one`, `insert_many` |
| lab 2 | Query operators like `$gt`, updating and deleting documents |
| lab 3 | Embed or reference, schema validation, `$group` with aggregate |

These need MongoDB running on `localhost:27017` with a `webshop` database, and `pymongo` installed.

    pip install pymongo
    python "MongoDB/lab 1/basics.py"
