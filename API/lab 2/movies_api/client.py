import os
from dotenv import load_dotenv
from api_client import get_json
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

# constant Variable
BASE_URL = "http://127.0.0.1:8000"

# # all movies
# movies = get_json(f"{BASE_URL}/movies")
# print(movies)


# # movie that does not exist
# missing = get_json(f"{BASE_URL}/movies/99")
# print(missing)


# add a movie
new_movie = {
    "title": "Spider-Man",
    "director": "Sam Raimi",
    "year": 2002
}
response = requests.post(f"{BASE_URL}/movies", json=new_movie, headers={"X-API-KEY":API_KEY})
print(response.status_code)
print(response.json())


response = requests.post(f"{BASE_URL}/movies", json=new_movie)
print(response.status_code)
print(response.json())


# modify_movie = requests.patch(f"{BASE_URL}/movies/1", json={"year":2000}, timeout=5)
# response = modify_movie.json()
