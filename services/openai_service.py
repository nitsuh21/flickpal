import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

def get_conversational_response(movies, mood):
    movie_descriptions = "\n".join(
        [f"{i+1}. {movie.title}: {movie.overview}" for i, movie in enumerate(movies)]
    )
    prompt = (
        f"I want to recommend some movies for a {mood} mood. Here are some options:\n\n"
        f"{movie_descriptions}\n\n"
        "Please recommend these movies to the user in a friendly way."
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()
