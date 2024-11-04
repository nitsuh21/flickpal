from fastapi import APIRouter, HTTPException
from models import MovieRequest, RecommendationResponse
from services.movie_service import get_movies_from_tmdb
from services.openai_service import get_conversational_response

router = APIRouter()

@router.post("/recommend-movies/", response_model=RecommendationResponse)
async def recommend_movies(movie_request: MovieRequest):
    try:
        movies = get_movies_from_tmdb(movie_request.genre, movie_request.num_recommendations)
    except HTTPException as e:
        print(e)
        raise e

    conversational_response = get_conversational_response(movies, movie_request.mood)
    
    return {"recommendations": conversational_response}
