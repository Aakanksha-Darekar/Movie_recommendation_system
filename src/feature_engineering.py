import pandas as pd

# Load cleaned data
df = pd.read_csv("C:/Users/admin/OneDrive/Desktop/6SEM/DMPM/movie_recommendation_system/dataset/cleaned_movie_metadata.csv")

def filter_by_genre(genre):
    """Returns movies matching the given genre."""
    return df[df['genres'].str.contains(genre, case=False, na=False)][['title', 'year', 'rating', 'runtime_(min)', 'genres']]

def search_by_keyword(keyword):
    """Returns movies where the title or genres contain the keyword."""
    return df[df.apply(lambda x: keyword.lower() in str(x['title']).lower() or keyword.lower() in str(x['genres']).lower(), axis=1)][['title', 'year', 'rating', 'runtime_(min)', 'genres']]