import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- API KEYS ---
TMDB_KEY = "24de9823f4c1b573c342df962c60e1ac"
TMDB_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNGRlOTgyM2Y0YzFiNTczYzM0MmRmOTYyYzYwZTFhYyIsIm5iZiI6MTc1NzMxNTI3OC4wOTIsInN1YiI6IjY4YmU4MGNlODM1NzQzYjNjNzA2YTI1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2jiYncJNr7_10mQinwqrBwg5VhwvDc8zzf9yYj8xc8Y"
OMDB_KEY = "2432f750"

def get_tmdb_movie(title):
    """Fetch movie info from TMDB by title"""
    headers = {"Authorization": f"Bearer {TMDB_TOKEN}"}
    tmdb_url = f"https://api.themoviedb.org/3/search/movie?query={title}&language=en-US&page=1"
    response = requests.get(tmdb_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            return data["results"][0]
    return {}

def get_omdb_movie(title):
    """Fetch movie info from OMDB by title"""
    omdb_url = f"https://www.omdbapi.com/?apikey={OMDB_KEY}&t={title}"
    response = requests.get(omdb_url)
    if response.status_code == 200:
        return response.json()
    return {}

def get_combined_movie(title):
    """Merge both TMDB and OMDB data into a single dictionary"""
    tmdb_data = get_tmdb_movie(title)
    omdb_data = get_omdb_movie(title)

    combined = {
        "title": omdb_data.get("Title") or tmdb_data.get("title"),
        "year": omdb_data.get("Year") or tmdb_data.get("release_date", "")[:4],
        "genre": omdb_data.get("Genre") or "N/A",
        "director": omdb_data.get("Director") or "N/A",
        "overview": tmdb_data.get("overview") or omdb_data.get("Plot"),
        "rating": omdb_data.get("imdbRating") or tmdb_data.get("vote_average"),
        "poster": (
            omdb_data.get("Poster")
            if omdb_data.get("Poster") and omdb_data.get("Poster") != "N/A"
            else f"https://image.tmdb.org/t/p/w500{tmdb_data.get('poster_path')}"
            if tmdb_data.get("poster_path")
            else None
        ),
        "backdrop": (
            f"https://image.tmdb.org/t/p/w780{tmdb_data.get('backdrop_path')}"
            if tmdb_data.get("backdrop_path")
            else None
        )
    }
    return combined


# Example usage
if __name__ == "__main__":
    movie = get_combined_movie("Inception")
    print(movie)
