from flask import Flask, render_template, request, jsonify
from db_config import init_db
from tmdb_utils import search_movies, get_movie_details, get_popular_movies, get_genres

app = Flask(__name__)
mysql = init_db(app)

@app.route('/')
def home():
    try:
        language = request.args.get('lang', 'en-US')
        popular_data = get_popular_movies(language)
        genres_data = get_genres()
        
        movies = popular_data.get('results', []) if popular_data else []
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
        return render_template('movie_details.html', movie=movie_data)
    except Exception as e:
        print(f"Error in movie_details route: {str(e)}")
        return render_template('error.html', message="Unable to load movie details."), 500

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/download_link')
def get_download_link():
    movie_id = request.args.get('movie_id')
    language = request.args.get('language')

    cur = mysql.connection.cursor()
    cur.execute("SELECT link FROM download_links WHERE movie_id=%s AND language=%s", (movie_id, language))
    result = cur.fetchone()
    cur.close()

    if result:
        return jsonify({'link': result[0]})
    else:
        return jsonify({'link': None, 'message': 'No legal link found.'})
