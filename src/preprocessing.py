import pandas as pd

# Load dataset
file_path = "../dataset/all_movies_dataset.csv"
df = pd.read_csv(file_path)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert columns to numeric
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Drop rows with missing values in critical columns
df.dropna(subset=['year', 'rating'], inplace=True)

# Save cleaned data
df.to_csv("../dataset/cleaned_movie_metadata.csv", index=False)

print("Preprocessing complete. Cleaned data saved!")