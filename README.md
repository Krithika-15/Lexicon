# Lexicon - Course Solutions

My lab solutions and projects from Lexicon's Python & AI course. I add to this repo as new labs are assigned.

## Contents

| Folder | What is inside |
| --- | --- |
| [Python Foundations](Python%20Foundations/) | Labs 1-9 and the final project of the Python fundamentals block |
| [Database](Database/) | SQL labs, written against a small SQLite webshop database |

## Python Foundations

Nine labs, one folder each. Every `lab N` folder has one `Part_X.py` file per section of that lab's worksheet. The full list of parts is in the [Python Foundations README](Python%20Foundations/README.md).

| Lab | Topic |
| --- | --- |
| 1 | Python basics |
| 2 | Collections in Python |
| 3 | Control flow |
| 4 | Functions |
| 5 | Scope and flexible arguments |
| 6 | Pythonic Python |
| 7 | Classes and objects |
| 8 | Inheritance |
| 9 | Polymorphism and composition |

### Final project - Match Point Sports Centre

A command-line booking system for a sports centre with tennis courts, padel courts and yoga classes. Customers can register, log in, book courts, join classes and cancel their own bookings. See the [project README](Python%20Foundations/Match%20Point%20Sports%20Centre/README.md) for the features, booking rules and structure.

## Database

| Lab | Topic |
| --- | --- |
| 1 | SELECT basics: WHERE, ORDER BY, LIMIT and OFFSET, IN, LIKE, column aliases |

Each lab folder has a `.sql` file with the questions as comments and my query under each one. `lab 1` also has `webshop.db`, the SQLite database the queries run against (tables `customers` and `products`).

## How to run

You need Python 3.9 or newer. The labs use only the standard library, so there is nothing to install.

Run a single lab part:

    python "Python Foundations/lab 1/Part_A.py"

Run the Match Point project:

    cd "Python Foundations/Match Point Sports Centre"
    python main.py

For the SQL labs, open `Database/lab 1/webshop.db` in [DB Browser for SQLite](https://sqlitebrowser.org/), paste a query from `lab1.sql` into the Execute SQL tab and run it.
