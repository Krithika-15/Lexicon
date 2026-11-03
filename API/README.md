# API

My API labs. Day 1 was about calling other people's APIs, day 2 was about making my own.

## lab 1 - Calling APIs

`api_client.py` has my helper functions `get_json` and `post_json`. They wrap `requests` and print a simple message if the request times out, can't connect or gets an error back.

- `Part_1.py` - getting products from the Fake Store API and sorting them by price
- `Part_2.py` - finding a city's coordinates and getting the weather from Open-Meteo
- `Part_3.py` - listing a GitHub user's repos using a token from a `.env` file
- `Part_4.py` - the weather again, but the result is saved to a JSON file and reused for a while instead of calling the API every time

Part 3 needs a `.env` file in the lab folder with your own token:

    GITHUB_TOKEN=your_token_here

## lab 2 - Movies API with FastAPI

A small API for a list of movies, in `movies_api/main.py`. It has `GET`, `POST`, `PUT`, `PATCH` and `DELETE` routes. Anything that changes data needs an API key in the `X-API-Key` header. The movies are saved to `movies.json` so they are still there after a restart.

`client.py` calls the API with `requests` to try out the routes.

The API key goes in a `.env` file in the `movies_api` folder:

    API_KEY=pick_any_key

Start the server:

    cd "lab 2/movies_api"
    uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs to try it in the browser.

## Packages

    pip install requests python-dotenv fastapi uvicorn

The `.env` files and the saved JSON files are in `.gitignore`, so you have to create your own.
