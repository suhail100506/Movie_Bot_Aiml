# Quick Start Guide - Movie Bot

Get your movie bot up and running in 5 minutes!

## Prerequisites Check

Before starting, ensure you have:
- ✅ Python 3.8 or higher
- ✅ MySQL Server installed and running
- ✅ pip (Python package manager)

## Step-by-Step Setup

### 1. Install Dependencies (1 minute)

Open terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- flask-mysqldb (database connector)
- requests (HTTP library)

### 2. Setup Database (2 minutes)

**Option A: Using MySQL Command Line**
```bash
mysql -u root -p < setup_database.sql
```

**Option B: Using MySQL Workbench**
1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Open `setup_database.sql`
4. Execute the script

**Option C: Manual Setup**
```sql
CREATE DATABASE movie_recommendation;
USE movie_recommendation;

CREATE TABLE download_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    movie_title VARCHAR(255) NOT NULL,
    language VARCHAR(10) NOT NULL,
    link VARCHAR(500) NOT NULL,
    quality VARCHAR(50),
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Configure Database Connection (30 seconds)

Edit `db_config.py` with your MySQL credentials:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'your_password'  # Your MySQL password
app.config['MYSQL_DB'] = 'movie_recommendation'
```

### 4. Run the Application (30 seconds)

```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### 5. Access the Application (30 seconds)

Open your browser and go to:
```
http://localhost:5000
```

🎉 **Congratulations!** Your movie bot is now running!

---

## Quick Feature Tour

### Browse Popular Movies
- Visit: `http://localhost:5000`
- See popular movies from TMDB

### Search for Movies
- Click the search icon (🔍) in the navigation bar
- Enter a movie name
- Press Enter

### Browse by Language
- Use the language dropdown in the navigation bar
- Select: English, Hindi, Tamil, Telugu, Malayalam, Kannada, etc.
- Or visit directly: `http://localhost:5000/language/hi` (for Hindi)

### View Trending Movies
- Click "Trending" in the navigation bar
- Or visit: `http://localhost:5000/trending`
- Switch between "Today" and "This Week"

### Get Movie Details & Download Links
1. Click on any movie card
2. View full movie details
3. Click "Get Download Links" button
4. Choose from multiple download sources

---

## Common Issues & Solutions

### Issue 1: "Module not found" error
**Solution:** Install missing packages
```bash
pip install flask flask-mysqldb requests
```

### Issue 2: "Can't connect to MySQL server"
**Solution:** 
1. Check if MySQL is running
2. Verify credentials in `db_config.py`
3. Test connection:
```bash
mysql -u root -p
```

### Issue 3: "No movies displayed"
**Solution:**
1. Check internet connection (TMDB API requires internet)
2. Verify TMDB API key is valid (already included in code)
3. Check browser console for errors (F12)

### Issue 4: Port 5000 already in use
**Solution:** Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001 instead
```

### Issue 5: Database connection error
**Solution:** Ensure MySQL service is running:
- **Windows:** Services → MySQL → Start
- **Mac:** `brew services start mysql`
- **Linux:** `sudo systemctl start mysql`

---

## Testing the Features

### Test 1: Search Functionality
```
1. Click search icon
2. Type "Inception"
3. Verify results appear
```

### Test 2: Language Filter
```
1. Select "Hindi" from language dropdown
2. Verify Hindi movies are displayed
3. URL should be: /language/hi
```

### Test 3: Download Links
```
1. Click any movie
2. Click "Get Download Links"
3. Verify multiple sources appear
4. Click "Visit" on any source
```

### Test 4: Trending Movies
```
1. Click "Trending" in navbar
2. Verify trending movies load
3. Switch between "Today" and "This Week"
```

---

## Next Steps

### Add Custom Download Links
```sql
INSERT INTO download_links (movie_id, movie_title, language, link, quality, source)
VALUES (550, 'Fight Club', 'en', 'https://your-link.com', '1080p', 'Custom');
```

### Customize the Design
- Edit `static/css/style.css` for styling
- Modify templates in `templates/` folder

### Add More Languages
- Edit `LANGUAGES` dictionary in `app.py`
- Add language options in templates

### Enable User Features
- Implement user authentication
- Add watchlist functionality
- Create user preferences

---

## Useful Commands

### Start the application
```bash
python app.py
```

### Stop the application
```
Press Ctrl+C in terminal
```

### Check MySQL connection
```bash
mysql -u root -p -e "USE movie_recommendation; SHOW TABLES;"
```

### View application logs
```bash
# Logs appear in terminal where app is running
```

### Clear browser cache
```
Ctrl+Shift+Delete (Windows/Linux)
Cmd+Shift+Delete (Mac)
```

---

## Development Tips

### Enable Debug Mode
Already enabled in `app.py`:
```python
app.run(debug=True)
```

### Auto-reload on Changes
Flask automatically reloads when you save files in debug mode

### View Database Data
```sql
USE movie_recommendation;
SELECT * FROM download_links;
```

### Test API Endpoints
Use browser or curl:
```bash
curl http://localhost:5000/api/languages
```

---

## Getting Help

### Check Logs
- Terminal output shows errors and requests
- Browser console (F12) shows JavaScript errors

### Common Log Messages
- ✅ `GET / 200` - Successful request
- ❌ `GET / 500` - Server error
- ⚠️ `Connection error` - Network/API issue

### Resources
- TMDB API Docs: https://developers.themoviedb.org/3
- Flask Docs: https://flask.palletsprojects.com/
- MySQL Docs: https://dev.mysql.com/doc/

---

## Production Deployment (Optional)

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## Summary

You now have a fully functional movie bot that can:
- ✅ Fetch movies from TMDB API
- ✅ Filter by 11+ languages
- ✅ Show trending movies
- ✅ Provide download links
- ✅ Display detailed movie information
- ✅ Search for any movie

**Enjoy exploring movies! 🎬🍿**
