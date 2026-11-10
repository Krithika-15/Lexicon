# Lexicon Course - My Solutions

This is where I keep my lab answers and projects from the Python & AI course at Lexicon. New folders get added as the course goes on.

## Folders

- [Python Foundations](Python%20Foundations/) - labs 1 to 9 and the Match Point final project
- [Database](Database/) - SQL labs in SQLite and a few MongoDB labs
- [API](API/) - calling APIs with `requests` and building a small API with FastAPI
- [Agile methods and Scrum](Agile%20methods%20and%20Scrum/) - written answers to the Agile and Scrum exercises
- [Data Analysis and visualisation](Data%20Analysis%20and%20visualisation/) - pandas labs in Jupyter notebooks, starting with Lab 1 on the Stockholm Airbnb listings

Each folder has its own README with more details and how to run things.

## Setup

I use Python 3.13 on Windows. The Python Foundations labs only need plain Python. The other folders need a few packages:

    pip install requests python-dotenv fastapi uvicorn pymongo pandas matplotlib seaborn jupyter

For the SQL labs I use [DB Browser for SQLite](https://sqlitebrowser.org/), and for the MongoDB labs a local MongoDB server.

The data analysis notebooks read `data/listings.csv`, which is not in the repo (it's large and comes from the course). To run them, put the file in a `data` folder next to the notebook.
