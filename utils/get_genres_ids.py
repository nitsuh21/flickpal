import requests
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Settings

# Replace with your TMDb API key
API_KEY = Settings.TMDB_API_KEY
BASE_URL = 'https://api.themoviedb.org/3'

def get_genre_id(genre_name):
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        'api_key': API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        genres = response.json().get('genres', [])
        
        # Find the genre ID that matches the genre name
        for genre in genres:
            if genre['name'].lower() == genre_name.lower():
                return genre['id']
        return f"Genre '{genre_name}' not found."
    else:
        return f"Failed to fetch genres: {response.status_code}"

# Example usage
genre_name = 'Action'
genre_id = get_genre_id(genre_name)
print(f"Genre ID for '{genre_name}': {genre_id}")
import requests

# Replace with your TMDb API key
API_KEY = 'your_tmdb_api_key'
BASE_URL = 'https://api.themoviedb.org/3'

def get_genre_id(genre_name):
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        'api_key': API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        genres = response.json().get('genres', [])
        
        # Find the genre ID that matches the genre name
        for genre in genres:
            if genre['name'].lower() == genre_name.lower():
                with open('genre_ids.json', 'w') as f:
                    json.dump(genres, f)
        return f"Genre '{genre_name}' not found."
    else:
        return f"Failed to fetch genres: {response.status_code}"

# Example usage
genre_name = 'Action'
genre_id = get_genre_id(genre_name)
print(f"Genre ID for '{genre_name}': {genre_id}")
