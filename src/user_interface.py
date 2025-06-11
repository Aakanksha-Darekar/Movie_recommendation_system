from src.feature_engineering import filter_by_genre, search_by_keyword
from src.recommendation import get_similar_movies

def user_interface():
    print("\nMovie Recommendation System")
    print("1. Search by Genre")
    print("2. Search by Keyword")
    print("3. Get Similar Movies by Title")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        genre = input("Enter genre (e.g., Action, Comedy, Drama): ")
        print(filter_by_genre(genre))

    elif choice == '2':
        keyword = input("Enter keyword (e.g., movie title or related word): ")
        print(search_by_keyword(keyword))

    elif choice == '3':
        movie_title = input("Enter movie title: ")
        print(get_similar_movies(movie_title))

    else:
        print("Invalid choice! Please select a valid option.")

# Run the user interface
if __name__ == "__main__":
    user_interface()