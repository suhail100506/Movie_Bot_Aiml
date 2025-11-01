def recommend_by_genre(user_genre, movies):
    return [m for m in movies if user_genre.lower() in [g['name'].lower() for g in m.get('genres', [])]]
