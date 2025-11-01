# Movie Bot - Multi-Language Movie Discovery & Download Platform

A comprehensive Flask-based movie discovery platform that fetches movies from TMDB API in multiple languages and provides download links.

## Features

### 🎬 Core Features
- **Multi-Language Support**: Browse movies in 11+ languages (English, Hindi, Tamil, Telugu, Malayalam, Kannada, Spanish, French, German, Japanese, Korean)
- **Movie Discovery**: Search and discover movies with advanced filters
- **Trending Movies**: View daily and weekly trending movies
- **Genre Filtering**: Filter movies by genres
- **Movie Details**: Comprehensive movie information including ratings, cast, budget, revenue
- **Download Links**: Multiple download sources for each movie
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### 🌍 Language-Specific Features
- Filter movies by original language
- Dedicated pages for regional cinema (Bollywood, Kollywood, Tollywood, etc.)
- Language-specific movie recommendations

### 📥 Download Features
- Multiple download sources (YTS, 1337x, RARBG, The Pirate Bay)
- Quality indicators (HD, 1080p, 720p, etc.)
- Direct links to trusted torrent sites
- Database-backed custom download links

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **API**: TMDB (The Movie Database)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- TMDB API Key (already included)

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd movie_bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Database**
- Update `db_config.py` with your MySQL credentials
- Run the SQL setup script:
```bash
mysql -u root -p < setup_database.sql
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
- Open browser and navigate to: `http://localhost:5000`

## API Endpoints

### Main Routes
- `GET /` - Home page with popular movies
- `GET /search?query=<movie_name>` - Search movies
- `GET /movie/<movie_id>` - Movie details page
- `GET /trending?time=<day|week>` - Trending movies
- `GET /language/<lang_code>` - Movies by language
- `GET /discover?genres=<ids>&sort_by=<option>` - Discover movies with filters

### API Routes
- `GET /api/languages` - Get supported languages
- `GET /download_link?movie_id=<id>&language=<lang>&title=<title>` - Get download links

## Supported Languages

| Code | Language |
|------|----------|
| en   | English  |
| hi   | Hindi    |
| ta   | Tamil    |
| te   | Telugu   |
| ml   | Malayalam|
| kn   | Kannada  |
| es   | Spanish  |
| fr   | French   |
| de   | German   |
| ja   | Japanese |
| ko   | Korean   |

## Database Schema

### download_links
- `id`: Primary key
- `movie_id`: TMDB movie ID
- `movie_title`: Movie title
- `language`: Language code
- `link`: Download URL
- `quality`: Video quality
- `source`: Source name

### user_preferences
- `id`: Primary key
- `user_id`: User identifier
- `preferred_languages`: JSON array of language codes
- `preferred_genres`: JSON array of genre IDs

### movie_cache
- `id`: Primary key
- `movie_id`: TMDB movie ID
- `movie_data`: Cached movie JSON data
- `language`: Language code

## Usage Examples

### Browse Movies by Language
```
http://localhost:5000/language/hi  # Hindi movies
http://localhost:5000/language/ta  # Tamil movies
http://localhost:5000/language/te  # Telugu movies
```

### View Trending Movies
```
http://localhost:5000/trending?time=day   # Today's trending
http://localhost:5000/trending?time=week  # This week's trending
```

### Search Movies
```
http://localhost:5000/search?query=Inception
```

### Discover with Filters
```
http://localhost:5000/discover?genres=28,12&sort_by=popularity.desc
```

## Features in Detail

### 1. Multi-Language Movie Discovery
- Fetch movies in 11+ languages
- Filter by original language
- Language-specific trending movies

### 2. Advanced Search & Filters
- Search by movie title
- Filter by genre, year, rating
- Sort by popularity, rating, release date

### 3. Download Links
- Multiple trusted sources
- Quality indicators
- Fallback to alternative sources
- Database-backed custom links

### 4. Movie Details
- Full movie information
- Cast and crew
- Budget and revenue
- User ratings
- Trailers and videos

## Configuration

### Database Configuration (db_config.py)
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'movie_recommendation'
```

### TMDB API (tmdb_utils.py)
- API Key and Access Token are already configured
- Rate limiting and retry logic implemented
- Error handling for network issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is for educational purposes only.

## Disclaimer

⚠️ This application provides links to third-party torrent sites. Users are responsible for ensuring they comply with local laws regarding downloading copyrighted content. The developers do not host or distribute any copyrighted material.

## Support

For issues and questions, please open an issue on GitHub.

## Roadmap

- [ ] User authentication and profiles
- [ ] Watchlist and favorites
- [ ] Movie recommendations based on viewing history
- [ ] Subtitle download links
- [ ] TV shows support
- [ ] Mobile app
- [ ] Advanced filtering options
- [ ] Social features (reviews, ratings)

---

**Built with ❤️ using Flask and TMDB API**