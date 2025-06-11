import streamlit as st
import pandas as pd
from src.feature_engineering import filter_by_genre, search_by_keyword
from src.recommendation import get_similar_movies

# Load dataset
file_path = "dataset/cleaned_movie_metadata.csv"
df = pd.read_csv(file_path)

# 🎥 Background Video (Ensure Correct Path)
video_file = "video2.mp4"

# 🔄 **Embed the Video Properly in Streamlit**
def background_video():
    try:
        with open(video_file, "rb") as vid_file:
            video_bytes = vid_file.read()
        st.video(video_bytes, format="video/mp4")
    except FileNotFoundError:
        st.error("Video file not found! Please check if 'video1.mp4' exists in the project folder.")

# 🔍 Main UI with Movie Recommendations
def main():
    background_video()  # Render background video FIRST

    st.title("🎬 Movie Recommendation System")
    st.sidebar.header("Filter Options")

    # 📌 Genre filter using feature_engineering.py
    genre = st.sidebar.selectbox("Select Genre", df['genres'].unique())
    if st.sidebar.button("Get Movies by Genre"):
        movies = filter_by_genre(genre)
        st.write(movies)

    # 🔍 Keyword search using feature_engineering.py
    keyword = st.sidebar.text_input("Enter a keyword or movie title")
    if st.sidebar.button("Search Movies"):
        movies = search_by_keyword(keyword)
        st.write(movies)

    # 🎞️ Similar movie recommendations using recommendation.py
    movie_title = st.sidebar.text_input("Find similar movies to:")
    if st.sidebar.button("Find Similar"):
        movies = get_similar_movies(movie_title)
        st.write(movies)

if __name__ == "__main__":
    main()