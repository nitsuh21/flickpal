import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")

settings = Settings()
