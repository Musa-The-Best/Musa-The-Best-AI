import random
# Sample movie list with genre, mood, and IMDb rating
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "mood": "Mind-bending", "rating": 8.8},
    {"title": "Forrest Gump", "genre": "Drama", "mood": "Heartwarming", "rating": 8.8},
    {"title": "Mad Max", "genre": "Action", "mood": "Exciting", "rating": 8.1},
]

# Function to recommend a movie
def recommend_movie(genre, mood, min_rating):
    matched = [
        movie for movie in movies
        if movie["genre"].lower() == genre.lower()
        and movie["mood"].lower() == mood.lower()
        and movie["rating"] >= min_rating
    ]
    return random.choice(matched)["title"] if matched else "No matching movie found."

# User input
print("🎬 Welcome to the Random Movie Recommender!")
genre_input = input("Enter your favorite genre (e.g., Drama, Action): ")
mood_input = input("Enter your current mood (e.g., Exciting, Heartwarming): ")
rating_input = input("Enter minimum IMDb rating (0–10): ")

# Convert rating input safely
try:
    rating_value = float(rating_input)
except ValueError:
    rating_value = 0.0

# Recommend and display movie
movie = recommend_movie(genre_input, mood_input, rating_value)
print(f"\n🎥 Recommended Movie: {movie}")
