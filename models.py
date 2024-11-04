from pydantic import BaseModel, Field
from typing import List, Optional

class MovieRequest(BaseModel):
    genre: str
    mood: Optional[str] = Field(default="default", description="Mood or tone for recommendations")
    num_recommendations: int = Field(default=5, description="Number of movie recommendations")

class MovieRecommendation(BaseModel):
    title: str
    overview: str

class RecommendationResponse(BaseModel):
    recommendations: List[MovieRecommendation]
