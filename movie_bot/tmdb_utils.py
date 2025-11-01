import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time

TMDB_API_KEY = '24de9823f4c1b573c342df962c60e1ac'
TMDB_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNGRlOTgyM2Y0YzFiNTczYzM0MmRmOTYyYzYwZTFhYyIsIm5iZiI6MTc1NzMxNTI3OC4wOTIsInN1YiI6IjY4YmU4MGNlODM1NzQzYjNjNzA2YTI1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2jiYncJNr7_10mQinwqrBwg5VhwvDc8zzf9yYj8xc8Y'

def create_session_with_retries():
    """Create a requests session with retry logic"""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def make_api_request(url, headers, max_retries=3):
    """Make API request with error handling and retries"""
    for attempt in range(max_retries):
        try:
            session = create_session_with_retries()
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error (attempt {attempt + 1}/{max_retries}): {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                return {'results': [], 'genres': []}
        except requests.exceptions.Timeout:
            print(f"Timeout error (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return {'results': [], 'genres': []}
        except requests.exceptions.RequestException as e:
            print(f"Request error: {str(e)}")
            return {'results': [], 'genres': []}
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return {'results': [], 'genres': []}
    
    return {'results': [], 'genres': []}

def search_movies(query, language='en-US'):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/search/movie?query={query}&language={language}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_movie_details(movie_id, language='en-US'):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?language={language}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_popular_movies(language='en-US', page=1):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/movie/popular?language={language}&page={page}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_genres():
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def discover_movies(language='en-US', page=1, genre_ids=None, sort_by='popularity.desc', year=None, from_date=None, to_date=None, **kwargs):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/discover/movie?language={language}&page={page}&sort_by={sort_by}&api_key={TMDB_API_KEY}'
    if genre_ids:
        url += f'&with_genres={genre_ids}'
    if year:
        url += f'&primary_release_year={year}'
    if from_date:
        url += f'&primary_release_date.gte={from_date}'
    if to_date:
        url += f'&primary_release_date.lte={to_date}'
    for key, value in kwargs.items():
        if value:
            url += f'&{key}={value}'
    return make_api_request(url, headers)

def get_movies_by_language(language_code, page=1):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/discover/movie?with_original_language={language_code}&sort_by=popularity.desc&page={page}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_trending_movies(time_window='week', language='en-US', page=1):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/trending/movie/{time_window}?language={language}&page={page}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_movie_videos(movie_id, language='en-US'):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?language={language}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_movie_credits(movie_id):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)

def get_movie_reviews(movie_id, page=1):
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews?page={page}&api_key={TMDB_API_KEY}'
    return make_api_request(url, headers)
