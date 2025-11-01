from flask import Flask, render_template, request, jsonify
from db_config import init_db
from tmdb_utils import (search_movies, get_movie_details, get_popular_movies, get_genres,
                        discover_movies, get_movies_by_language, get_trending_movies, get_movie_videos,
                        get_movie_credits, get_movie_reviews)
import requests

app = Flask(__name__)
mysql = init_db(app)

LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ml': 'Malayalam',
    'kn': 'Kannada',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'ja': 'Japanese',
    'ko': 'Korean'
}

@app.route('/')
def home():
    try:
        language = request.args.get('lang', 'en-US')
        page = request.args.get('page', 1, type=int)
        popular_data = get_popular_movies(language, page)
        genres_data = get_genres()
        
        movies = popular_data.get('results', []) if popular_data else []
        movies = sorted(movies, key=lambda x: x.get('release_date', ''), reverse=True)
        genres = genres_data.get('genres', []) if genres_data else []
        
        return render_template('home.html', movies=movies, genres=genres, error=None)
    except Exception as e:
        print(f"Error in home route: {str(e)}")
        return render_template('home.html', movies=[], genres=[], error="Unable to load movies. Please try again later.")

@app.route('/search')
def search():
    try:
        query = request.args.get('query')
        language = request.args.get('lang', 'en-US')
        data = search_movies(query, language)
        movies = data.get('results', []) if data else []
        movies = sorted(movies, key=lambda x: x.get('release_date', ''), reverse=True)
        return render_template('movies.html', movies=movies, error=None)
    except Exception as e:
        print(f"Error in search route: {str(e)}")
        return render_template('movies.html', movies=[], error="Search failed. Please try again.")

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    try:
        language = request.args.get('lang', 'en-US')
        movie_data = get_movie_details(movie_id, language)
        if not movie_data or 'id' not in movie_data:
            return render_template('error.html', message="Movie not found."), 404
        
        credits_data = get_movie_credits(movie_id)
        reviews_data = get_movie_reviews(movie_id)
        
        cast = credits_data.get('cast', [])[:10] if credits_data else []
        crew = credits_data.get('crew', []) if credits_data else []
        reviews = reviews_data.get('results', []) if reviews_data else []
        
        return render_template('movie_details.html', movie=movie_data, cast=cast, crew=crew, reviews=reviews)
    except Exception as e:
        print(f"Error in movie_details route: {str(e)}")
        return render_template('error.html', message="Unable to load movie details."), 500

@app.route('/discover')
def discover():
    try:
        language = request.args.get('lang', 'en-US')
        genre_ids = request.args.get('genres')
        sort_by = request.args.get('sort_by', 'release_date.desc')
        page = request.args.get('page', 1, type=int)
        year = request.args.get('year')
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        
        extra_params = {}
        if request.args.get('with_original_language'):
            extra_params['with_original_language'] = request.args.get('with_original_language')
        if request.args.get('vote_average_gte'):
            extra_params['vote_average.gte'] = request.args.get('vote_average_gte')
        if request.args.get('vote_count_gte'):
            extra_params['vote_count.gte'] = request.args.get('vote_count_gte')
        if request.args.get('with_runtime_gte'):
            extra_params['with_runtime.gte'] = request.args.get('with_runtime_gte')
        if request.args.get('keywords'):
            extra_params['with_keywords'] = request.args.get('keywords')
        
        data = discover_movies(language, page, genre_ids, sort_by, year, from_date, to_date, **extra_params)
        genres_data = get_genres()
        
        movies = data.get('results', []) if data else []
        genres = genres_data.get('genres', []) if genres_data else []
        
        return render_template('home.html', movies=movies, genres=genres, error=None)
    except Exception as e:
        print(f"Error in discover route: {str(e)}")
        return render_template('home.html', movies=[], genres=[], error="Unable to discover movies.")

@app.route('/sort')
def sort_movies():
    try:
        sort_by = request.args.get('by', 'release_date.desc')
        language = request.args.get('lang', 'en-US')
        page = request.args.get('page', 1, type=int)
        
        data = discover_movies(language, page, None, sort_by)
        genres_data = get_genres()
        
        movies = data.get('results', []) if data else []
        genres = genres_data.get('genres', []) if genres_data else []
        
        return render_template('home.html', movies=movies, genres=genres, error=None)
    except Exception as e:
        print(f"Error in sort route: {str(e)}")
        return render_template('home.html', movies=[], genres=[], error="Unable to sort movies.")

@app.route('/language/<lang_code>')
def movies_by_language(lang_code):
    try:
        page = request.args.get('page', 1, type=int)
        data = get_movies_by_language(lang_code, page)
        genres_data = get_genres()
        
        movies = data.get('results', []) if data else []
        movies = sorted(movies, key=lambda x: x.get('release_date', ''), reverse=True)
        genres = genres_data.get('genres', []) if genres_data else []
        language_name = LANGUAGES.get(lang_code, lang_code.upper())
        
        return render_template('language_movies.html', movies=movies, genres=genres, 
                             language=language_name, lang_code=lang_code, error=None)
    except Exception as e:
        print(f"Error in language route: {str(e)}")
        return render_template('language_movies.html', movies=[], genres=[], 
                             language=lang_code, lang_code=lang_code, error="Unable to load movies.")

@app.route('/trending')
def trending():
    try:
        time_window = request.args.get('time', 'week')
        language = request.args.get('lang', 'en-US')
        page = request.args.get('page', 1, type=int)
        data = get_trending_movies(time_window, language, page)
        genres_data = get_genres()
        
        movies = data.get('results', []) if data else []
        genres = genres_data.get('genres', []) if genres_data else []
        
        return render_template('trending.html', movies=movies, genres=genres, 
                             time_window=time_window, error=None)
    except Exception as e:
        print(f"Error in trending route: {str(e)}")
        return render_template('trending.html', movies=[], genres=[], 
                             time_window='week', error="Unable to load trending movies.")

@app.route('/api/languages')
def get_languages():
    return jsonify(LANGUAGES)

@app.route('/download_link')
def get_download_link():
    movie_id = request.args.get('movie_id')
    language = request.args.get('language')
    movie_title = request.args.get('title', '')
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT link FROM download_links WHERE movie_id=%s AND language=%s", (movie_id, language))
        result = cur.fetchone()
        cur.close()
        
        if result:
            return jsonify({'link': result[0], 'source': 'database'})
        else:
            # Generate alternative download sources
            alternative_links = generate_download_links(movie_id, movie_title)
            return jsonify({'links': alternative_links, 'message': 'Multiple sources available'})
    except Exception as e:
        print(f"Error fetching download link: {str(e)}")
        alternative_links = generate_download_links(movie_id, movie_title)
        return jsonify({'links': alternative_links, 'message': 'Alternative sources'})

def generate_download_links(movie_id, movie_title):
    """Generate alternative download source links"""
    safe_title = movie_title.replace(' ', '+')
    return [
        {'name': 'YTS', 'url': f'https://yts.mx/browse-movies/{safe_title}', 'quality': 'HD'},
        {'name': '1337x', 'url': f'https://1337x.to/search/{safe_title}/1/', 'quality': 'Various'},
        {'name': 'RARBG', 'url': f'https://rarbg.to/torrents.php?search={safe_title}', 'quality': 'HD'},
        {'name': 'The Pirate Bay', 'url': f'https://thepiratebay.org/search.php?q={safe_title}', 'quality': 'Various'}
    ]

@app.route('/filter')
def filter_movies():
    try:
        sort_by = request.args.get('sort_by', 'release_date.desc')
        genre_ids = request.args.get('genres')
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        language = request.args.get('lang', 'en-US')
        page = request.args.get('page', 1, type=int)
        
        extra_params = {}
        if request.args.get('with_original_language'):
            extra_params['with_original_language'] = request.args.get('with_original_language')
        if request.args.get('vote_average_gte'):
            extra_params['vote_average.gte'] = request.args.get('vote_average_gte')
        if request.args.get('vote_count_gte'):
            extra_params['vote_count.gte'] = request.args.get('vote_count_gte')
        if request.args.get('with_runtime_gte'):
            extra_params['with_runtime.gte'] = request.args.get('with_runtime_gte')
        
        data = discover_movies(language, page, genre_ids, sort_by, None, from_date, to_date, **extra_params)
        genres_data = get_genres()
        
        movies = data.get('results', []) if data else []
        genres = genres_data.get('genres', []) if genres_data else []
        
        return render_template('home.html', movies=movies, genres=genres, error=None)
    except Exception as e:
        print(f"Error in filter route: {str(e)}")
        return render_template('home.html', movies=[], genres=[], error="Unable to filter movies.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
