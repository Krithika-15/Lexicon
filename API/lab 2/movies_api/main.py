import os
import json
from dotenv import load_dotenv

from fastapi import Depends, Header, FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()
API_KEY = os.getenv("API_KEY")
MOVIES_FILE = "movies.json"

def check_key(x_api_key: str | None = Header(default=None)):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key or missing API key")


app = FastAPI()

# Part 1
# 1 Start the server
STARTING_MOVIES = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "director": "Chris Columbus", "year": 2001},
    {"id": 2, "title": "The Avengers", "director": "Joss Whedon", "year": 2012},
    {"id": 3, "title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "director": "Andrew Adamson", "year": 2005},
    {"id": 4, "title": "Wonder Woman", "director": "Patty Jenkins", "year": 2017},
]


# Part 4 : 1 helper function
def load_movies():
    if os.path.exists(MOVIES_FILE):
        with open(MOVIES_FILE, encoding="utf-8") as f:
            data = json.load(f)
            return data
    return STARTING_MOVIES

# Part 4 : 1 helper function
def save_movies():
    with open(MOVIES_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)


# Part 4 : 1 helper function
movies = load_movies()

class Movie(BaseModel):
    title: str
    director: str
    year: int


# Part 2 : 1 Model
class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


def find_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

# 2 Get one movie
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

# Test
# /movies/1 => 200 OK
# /movies/7 => 404 Not Found
# /movies/abc => 422 Invalid data
    # In FastAPI Swagger UI :
    # Please correct the following validation errors and try again.
    # For 'movie_id': Value must be an integer.



# 3 Filter with a query parameter
@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    result = []
    for movie in movies:
        if director is not None and director.lower() not in movie["director"].lower():
            continue
        if year is not None and movie["year"] != year:
            continue
        result.append(movie)
    return result


# Test
# /movies                            => 200, all 4 movies
# /movies?director=whedon            => 200, The Avengers
# /movies?year=2005                  => 200, Narnia
# /movies?director=scott             => 200, [] (no Ridley Scott film in my list)
# /movies?year=1999                  => 200, []
# /movies?director=whedon&year=2012  => 200, The Avengers
# /movies?year=abc                   => 422, loc: ["query", "year"]
# => {"detail":[{"type":"int_parsing","loc":["query","year"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}



# 4  Add a movie
@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def add_movie(movie: Movie):
    # find the biggest id
    biggest_id = 0
    for existing_movie in movies:
        if existing_movie["id"] > biggest_id:
            biggest_id = existing_movie["id"]

    # build the new movie as a dictionary
    new_movie = {
        "id": biggest_id + 1,
        "title": movie.title,
        "director": movie.director,
        "year": movie.year
    }

    # adding new movie to the list
    movies.append(new_movie)

    # write the updated list to movies.json # Part 4: 2
    save_movies()

    # also return the new movie
    return new_movie


# Test
# In Swagger UI:

# with complete data  ==> 201, Created
# {
#   "title": "The Dark Knight",
#   "director": "Christopher Nolan",
#   "year": 2008
# }

# without director name ==> 422, Error: Unprocessable Content
# {
#   "title": "Inception",
#   "year": 2010
# }

# with year as string ==> 422, Error: Unprocessable Content
# {
#   "title": "Inception",
#   "director": "Christopher Nolan",
#   "year": "two thousand ten"
# }



# 5 replace and remove
@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    # write the updated list to movies.json # Part 4: 2
    save_movies()
    return existing

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)
    # write the updated list to movies.json # Part 4: 2
    save_movies()
    return None

# Test
# In swagger UI:
# Deleted movie id : 1 => 204 Successful Response
# Deleting same movie again => 404 Error: Not Found

# After server restarts, the newly added movies are gone and deleted ones are back.
# The list actually lives only in the server's memory (RAM), so it is rebuilt again
# from the hard-coded list every time the main.py runs.


# 6 Call your own API from python



# PART 2 : 1: route
@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def modify_movie(movie_id: int, changes: MovieUpdate):
    existing = find_movie(movie_id)
    existing.update(changes.model_dump(exclude_unset=True))
    # write the updated list to movies.json
    save_movies()
    return existing


# Part 2 : 3 test the edges
# Test
# In Swagger UI:

# PATCH /movies/1 with {"year": 2000}       => 200, only year changed
# GET   /movies/1                            => 200, title and director unchanged, year 2000

# PATCH /movies/1 with {}                    => 200, nothing changed
#   model_dump(exclude_unset=True) gives {}, so update({}) changes nothing

# PATCH /movies/1 with {"year": "abc"}       => 422 Unprocessable Content
#   Pydantic checks against MovieUpdate before my function runs

# PATCH /movies/99 with {"year": 2000}       => 404 Not Found
#   find_movie raises it

# Note: Swagger pre-fills every field with "string".
# Need to Delete the fields that I don't want to change, or they get sent too.


# part 2 : 4 Difference
# PUT replaces the whole movie, so the client must send every field (title, director, year).
# PATCH changes only the fields the client sends, e.g. fixing just the year of a movie.


# Part 4 : 3 Tested
# works good


# Part 4 : 4 Think
# 1. If two people add a movie at the same time, both can get the same id, and one
#    save can overwrite the other, so the first person's movie disappears silently.
# 2. A database hands out each id only once and uses transactions and locks,
#    so two writes at the same time can't overwrite each other.
