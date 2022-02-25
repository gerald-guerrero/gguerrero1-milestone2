import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def movie_data(movie_id):
    BASE_URL = "https://api.themoviedb.org/3/movie/" + str(movie_id)
    params = {"api_key": os.getenv("TMDB_KEY"), "language": "en-US"}

    response = requests.get(BASE_URL, params=params)

    response_json = response.json()
    try:
        title = response_json["title"]
    except:
        title = "title not found"

    try:
        tagline = response_json["tagline"]
    except:
        tagline = "tagline not found"

    try:
        genres_list = response_json["genres"]
        genres = ""
        for i in range(len(genres_list)):
            genres_list[i] = genres_list[i]["name"]
        genres = ", ".join(genres_list)
    except:
        genres = "genres not found"

    try:
        image = "https://image.tmdb.org/t/p/w500" + response_json["poster_path"]
    except:
        image = ""

    return title, tagline, genres, image
