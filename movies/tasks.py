import time

from celery import shared_task

from .models import Movie

# Fake movie data. No API key needed.
MOVIES = {
    "shutter island": {
        "title": "Shutter Island",
        "release_year": 2010,
        "director": "Martin Scorsese",
        "genre": "Thriller",
        "rating": 8.2,
    },
    "inception": {
        "title": "Inception",
        "release_year": 2010,
        "director": "Christopher Nolan",
        "genre": "Sci-Fi",
        "rating": 8.8,
    },
    "predestination": {
        "title": "Predestination",
        "release_year": 2014,
        "director": "Michael and Peter Spierig",
        "genre": "Sci-Fi",
        "rating": 7.4,
    },
}


@shared_task
def lookup_movie(movie_id):
    time.sleep(2)

    movie = Movie.objects.get(id=movie_id)
    info = MOVIES.get(movie.title.lower())

    if info:
        movie.title = info["title"]
        movie.release_year = info["release_year"]
        movie.director = info["director"]
        movie.genre = info["genre"]
        movie.rating = info["rating"]
    else:
        movie.director = "Unknown"
        movie.genre = "Unknown"
        movie.release_year = 0
        movie.rating = 0

    movie.status = "done"
    movie.save()
