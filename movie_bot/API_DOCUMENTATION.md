# Movie Bot API Documentation

## Base URL
```
http://localhost:5000
```

## Endpoints

### 1. Home Page
**Endpoint:** `GET /`

**Description:** Displays popular movies with genre filters

**Query Parameters:**
- `lang` (optional): Language code (default: 'en-US')
  - Example: `en-US`, `hi-IN`, `ta-IN`

**Example:**
```
GET /?lang=hi-IN
```

**Response:** HTML page with popular movies

---

### 2. Search Movies
**Endpoint:** `GET /search`

**Description:** Search for movies by title

**Query Parameters:**
- `query` (required): Movie title to search
- `lang` (optional): Language code (default: 'en-US')

**Example:**
```
GET /search?query=Inception&lang=en-US
```

**Response:** HTML page with search results

---

### 3. Movie Details
**Endpoint:** `GET /movie/<movie_id>`

**Description:** Get detailed information about a specific movie

**Path Parameters:**
- `movie_id` (required): TMDB movie ID

**Query Parameters:**
- `lang` (optional): Language code (default: 'en-US')

**Example:**
```
GET /movie/550?lang=en-US
```

**Response:** HTML page with movie details including:
- Title, poster, backdrop
- Rating, runtime, genres
- Overview, tagline
- Budget, revenue
- Production companies
- Download links

---

### 4. Discover Movies
**Endpoint:** `GET /discover`

**Description:** Discover movies with advanced filters

**Query Parameters:**
- `lang` (optional): Language code (default: 'en-US')
- `genres` (optional): Comma-separated genre IDs
- `sort_by` (optional): Sort option (default: 'popularity.desc')
  - Options: `popularity.desc`, `popularity.asc`, `vote_average.desc`, `release_date.desc`
- `page` (optional): Page number (default: 1)
- `year` (optional): Release year

**Example:**
```
GET /discover?genres=28,12&sort_by=popularity.desc&year=2023
```

**Response:** HTML page with filtered movies

---

### 5. Movies by Language
**Endpoint:** `GET /language/<lang_code>`

**Description:** Get movies in a specific language

**Path Parameters:**
- `lang_code` (required): Language code
  - Supported: `en`, `hi`, `ta`, `te`, `ml`, `kn`, `es`, `fr`, `de`, `ja`, `ko`

**Query Parameters:**
- `page` (optional): Page number (default: 1)

**Example:**
```
GET /language/hi?page=1
```

**Response:** HTML page with movies in specified language

---

### 6. Trending Movies
**Endpoint:** `GET /trending`

**Description:** Get trending movies

**Query Parameters:**
- `time` (optional): Time window (default: 'week')
  - Options: `day`, `week`
- `lang` (optional): Language code (default: 'en-US')

**Example:**
```
GET /trending?time=day&lang=en-US
```

**Response:** HTML page with trending movies

---

### 7. Get Languages (API)
**Endpoint:** `GET /api/languages`

**Description:** Get list of supported languages

**Example:**
```
GET /api/languages
```

**Response:**
```json
{
  "en": "English",
  "hi": "Hindi",
  "ta": "Tamil",
  "te": "Telugu",
  "ml": "Malayalam",
  "kn": "Kannada",
  "es": "Spanish",
  "fr": "French",
  "de": "German",
  "ja": "Japanese",
  "ko": "Korean"
}
```

---

### 8. Get Download Links (API)
**Endpoint:** `GET /download_link`

**Description:** Get download links for a movie

**Query Parameters:**
- `movie_id` (required): TMDB movie ID
- `language` (required): Language code
- `title` (optional): Movie title for generating links

**Example:**
```
GET /download_link?movie_id=550&language=en&title=Fight%20Club
```

**Response (Database Link):**
```json
{
  "link": "https://yts.mx/movies/fight-club-1999",
  "source": "database"
}
```

**Response (Alternative Links):**
```json
{
  "links": [
    {
      "name": "YTS",
      "url": "https://yts.mx/browse-movies/Fight+Club",
      "quality": "HD"
    },
    {
      "name": "1337x",
      "url": "https://1337x.to/search/Fight+Club/1/",
      "quality": "Various"
    },
    {
      "name": "RARBG",
      "url": "https://rarbg.to/torrents.php?search=Fight+Club",
      "quality": "HD"
    },
    {
      "name": "The Pirate Bay",
      "url": "https://thepiratebay.org/search.php?q=Fight+Club",
      "quality": "Various"
    }
  ],
  "message": "Multiple sources available"
}
```

---

## TMDB API Integration

### Functions Available (tmdb_utils.py)

#### 1. search_movies(query, language='en-US')
Search for movies by title

#### 2. get_movie_details(movie_id, language='en-US')
Get detailed information about a movie

#### 3. get_popular_movies(language='en-US', page=1)
Get popular movies

#### 4. get_genres()
Get list of movie genres

#### 5. discover_movies(language='en-US', page=1, genre_ids=None, sort_by='popularity.desc', year=None)
Discover movies with filters

#### 6. get_movies_by_language(language_code, page=1)
Get movies in a specific language

#### 7. get_trending_movies(time_window='week', language='en-US')
Get trending movies

#### 8. get_movie_videos(movie_id, language='en-US')
Get trailers and videos for a movie

---

## Error Handling

All endpoints include error handling and will return appropriate error messages:

- **Network Errors**: Retry logic with exponential backoff
- **API Errors**: Graceful fallback with empty results
- **Database Errors**: Alternative download sources provided

---

## Rate Limiting

The application implements:
- Retry logic for failed requests
- Exponential backoff for rate limits
- Connection pooling for better performance

---

## Language Codes

### Display Languages (for UI)
- `en-US`: English (United States)
- `hi-IN`: Hindi (India)
- `ta-IN`: Tamil (India)
- `te-IN`: Telugu (India)

### Original Languages (for filtering)
- `en`: English
- `hi`: Hindi
- `ta`: Tamil
- `te`: Telugu
- `ml`: Malayalam
- `kn`: Kannada
- `es`: Spanish
- `fr`: French
- `de`: German
- `ja`: Japanese
- `ko`: Korean

---

## Genre IDs

Common genre IDs from TMDB:
- 28: Action
- 12: Adventure
- 16: Animation
- 35: Comedy
- 80: Crime
- 99: Documentary
- 18: Drama
- 10751: Family
- 14: Fantasy
- 36: History
- 27: Horror
- 10402: Music
- 9648: Mystery
- 10749: Romance
- 878: Science Fiction
- 10770: TV Movie
- 53: Thriller
- 10752: War
- 37: Western

---

## Usage Examples

### Python Requests
```python
import requests

# Search for movies
response = requests.get('http://localhost:5000/search', params={'query': 'Inception'})

# Get movie details
response = requests.get('http://localhost:5000/movie/550')

# Get Hindi movies
response = requests.get('http://localhost:5000/language/hi')

# Get download links
response = requests.get('http://localhost:5000/download_link', params={
    'movie_id': 550,
    'language': 'en',
    'title': 'Fight Club'
})
data = response.json()
```

### JavaScript Fetch
```javascript
// Get download links
fetch('/download_link?movie_id=550&language=en&title=Fight%20Club')
  .then(response => response.json())
  .then(data => {
    if (data.links) {
      data.links.forEach(link => {
        console.log(`${link.name}: ${link.url}`);
      });
    }
  });

// Get languages
fetch('/api/languages')
  .then(response => response.json())
  .then(languages => {
    console.log(languages);
  });
```

---

## Best Practices

1. **Caching**: Implement caching for frequently accessed data
2. **Error Handling**: Always handle errors gracefully
3. **Rate Limiting**: Respect TMDB API rate limits
4. **User Experience**: Show loading states during API calls
5. **Security**: Validate all user inputs

---

## Support

For issues or questions, please refer to the main README.md or open an issue on GitHub.
