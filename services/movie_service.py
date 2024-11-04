import requests
from fastapi import HTTPException
from config import settings
from models import MovieRecommendation

TMDB_SEARCH_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={settings.TMDB_API_KEY}"

def get_movies_from_tmdb(genre, num_recommendations=5):
    print("input",genre, num_recommendations)
    response = requests.get(TMDB_SEARCH_URL, params={
        "with_genres": genre,
        "sort_by": "popularity.desc",
        "page": 1
    })

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch movies from TMDb")

    movies = response.json().get("results", [])[:num_recommendations]
    return [MovieRecommendation(title=movie["title"], overview=movie["overview"]) for movie in movies]
