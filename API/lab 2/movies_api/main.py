from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1 Start the server
movies = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "director": "Chris Columbus", "year": 2001},
    {"id": 2, "title": "The Avengers", "director": "Joss Whedon", "year": 2012},
    {"id": 3, "title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "director": "Andrew Adamson", "year": 2005},
    {"id": 4, "title": "Wonder Woman", "director": "Patty Jenkins", "year": 2017},
]


class Movie(BaseModel):
    title: str
    director: str
    year: int


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
@app.post("/movies", status_code=201)
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
@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    return existing

@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)
    return None

# Test
# In swagger UI:
# Deleted movie id : 1 => 204 Successful Response
# Deleting same movie again => 404 Error: Not Found

# After server restarts, the newly added movies are gone and deleted ones are back.
# The list actually lives only in the server's memory (RAM), so it is rebuilt again
# from the hard-coded list every time the main.py runs.


# 6 Call your own API from python
