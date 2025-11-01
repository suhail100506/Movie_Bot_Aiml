-- Create database
CREATE DATABASE IF NOT EXISTS movie_recommendation;
USE movie_recommendation;

-- Create download_links table
CREATE TABLE IF NOT EXISTS download_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    movie_title VARCHAR(255) NOT NULL,
    language VARCHAR(10) NOT NULL,
    link VARCHAR(500) NOT NULL,
    quality VARCHAR(50),
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_movie_id (movie_id),
    INDEX idx_language (language)
);

-- Create user_preferences table
CREATE TABLE IF NOT EXISTS user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    preferred_languages JSON,
    preferred_genres JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create movie_cache table for faster access
CREATE TABLE IF NOT EXISTS movie_cache (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL UNIQUE,
    movie_data JSON NOT NULL,
    language VARCHAR(10),
    cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_movie_id (movie_id),
    INDEX idx_language (language)
);

-- Insert sample download links
INSERT INTO download_links (movie_id, movie_title, language, link, quality, source) VALUES
(550, 'Fight Club', 'en', 'https://yts.mx/movies/fight-club-1999', '1080p', 'YTS'),
(278, 'The Shawshank Redemption', 'en', 'https://yts.mx/movies/the-shawshank-redemption-1994', '1080p', 'YTS'),
(238, 'The Godfather', 'en', 'https://yts.mx/movies/the-godfather-1972', '1080p', 'YTS');
