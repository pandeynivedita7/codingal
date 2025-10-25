import pandas as pd# array
import random# random movie
from sklearn.feature_extraction.text import TfidfVectorizer# matrix 
from sklearn.metrics.pairwise import cosine_similarity# pair

# Sample movie dataset
data = {# key and values to be working together i am using dict{key:values}
    'title': ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Avengers: Endgame'],#list mutable can be changed
    'genre': ['Sci-Fi, Action', 'Sci-Fi, Action', 'Sci-Fi, Drama', 'Action, Crime', 'Action, Superhero'],
    'description': [
        'A thief who steals corporate secrets through the use of dream-sharing technology.',
        'A hacker discovers the world is a simulation and fights to free humanity.',
        'A team travels through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'Batman battles the Joker who seeks to create chaos in Gotham.',
        'Superheroes assemble to undo the damage caused by Thanos.'
    ],
    'rating': [8.8, 8.7, 8.6, 9.0, 8.4]
}

movies_df = pd.DataFrame(data)

# Prepare TF-IDF vectorizer for AI-based recommendation
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies_df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def ai_recommend(movie_title):
    """Recommend the most similar movie based on description."""
    if movie_title not in movies_df['title'].values:
        print("Movie not found in database.")
        return None
    
    idx = movies_df.index[movies_df['title'] == movie_title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Skip the first movie (itself)
    movie_index = sim_scores[1][0]
    return movies_df.iloc[movie_index]

def random_recommend():
    """Return a random movie from the dataset."""
    return movies_df.sample(1).iloc[0]

# User interaction
print("Welcome to the Movie Recommendation System!")
choice = input("Choose recommendation type (AI / Random): ").strip().lower()

if choice == 'ai':
    movie_title = input("Enter a movie you like: ").strip()
    recommended = ai_recommend(movie_title)
elif choice == 'random':
    recommended = random_recommend()
else:
    print("Invalid choice. Please enter 'AI' or 'Random'.")
    recommended = None

# Display result
if recommended is not None:
    print("\n🎬 Recommended Movie:")
    print("-" * 40)
    print(f"Title       : {recommended['title']}")
    print(f"Genre       : {recommended['genre']}")
    print(f"Rating      : {recommended['rating']}")
    print(f"Description : {recommended['description']}")
    print("-" * 40)
