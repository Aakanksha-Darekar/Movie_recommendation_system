import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
df = pd.read_csv("C:/Users/admin/OneDrive/Desktop/6SEM/DMPM/movie_recommendation_system/dataset/cleaned_movie_metadata.csv")

# Convert genres into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
genre_matrix = vectorizer.fit_transform(df['genres'].fillna(''))

# Compute cosine similarity
similarity_matrix = cosine_similarity(genre_matrix)

def get_similar_movies(movie_title, n=5):
    """Returns top-N similar movies based on genres."""
    idx = df[df['title'].str.contains(movie_title, case=False, na=False)].index
    if len(idx) == 0:
        return "Movie not found!"
    
    idx = idx[0]  # Get first match
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]  # Get top N matches
    
    movie_indices = [i[0] for i in sim_scores]
    return df.iloc[movie_indices][['title', 'year', 'rating', 'runtime_(min)', 'genres']]