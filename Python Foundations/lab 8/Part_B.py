movie_dict = {
    "title": "Avengers: Endgame",
    "director": "Anthony and Joe Russo",
    "rating": 8.4
}

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        # rating is out of 10, in general above 8 is considered good and highly rated
        return self.rating >= 8

movie_object = Movie("Avengers: Endgame", "Anthony and Joe Russo", 8.4)
movie_1 = Movie("Avengers: Infinity War", "Anthony and Joe Russo", 8.4)
movie_2 = Movie("Green Lantern", "Martin Campbell", 5)
movie_3 = Movie("The Avengers", "Joss Whedon", 8.0)

for movie in [movie_object,movie_1, movie_2, movie_3]:
    print(f"Movie Title : {movie.title}\nDirector : {movie.director}\nHighly rated : {movie.is_highly_rated()}\n")

# Dictionary : stores data
# use when I just need to store simple data quickly
# also when I don't need any behaviour

# Class : stores data and behaviour
# use when the data needs behaviour and every object should have same structure
# in this case, each movie can check itself with is_highly_rated method
# In scenarios I want to create many movies with same structure
