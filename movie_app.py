import json
#import requests
from storage_json import StorageJson
import storage_cvs

#OMDB_API_KEY = "515cc4a9"


class MovieApp:
    def __init__(self, storage):
        def __init__(self, storage_type):
            if storage_type == "json":
                self._storage = StorageJson("../movies.json")
            elif storage_type == "csv":
                self._storage = storage_cvs.StorageCsv("movies.csv")
            else:
                raise ValueError("Invalid storage type. Supported types are 'json' and 'csv'.")

    def _command_list_movies(self):
        with open("../movies.json") as f:
            movies_data = json.load(f)
        print("Movie list:")
        for title, data in movies_data.items():
            print(f"{title} ({data['year']}) - rating: {data['rating']}")
        return movies_data

    def _command_movie_stats(self):
        with open("../movies.json") as f:
            movies_data = json.load(f)

        # Sort movies by rating in descending order
        sorted_movies = sorted(movies_data.items(), key=lambda x: x[1]['rating'], reverse=True)

        # Display movie statistics
        print("Movie statistics highest rating:")
        for title, data in sorted_movies:
            print(f"{title} ({data['year']}) - rating: {data['rating']}")

    """def _generate_website(self):
        # Load the list of movies
        movies_data = self._command_list_movies()

        # Create the movie grid HTML
        movie_grid_html = ""
        for movie_title, movie_info in movies_data.items():
            year = movie_info["year"]

            # Make a request to the OMDB API to get the movie details
            response = requests.get(f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={movie_title}")
            response_json = response.json()

            # Get the URL of the movie poster from the API response
            poster_url = response_json.get("Poster", "")

            movie_html = f'<li class="movie-item"><img src="{poster_url}"><div class="movie-title">{movie_title}</div><div class="movie-details"><span class="movie-year">{year}</span></div></li>'
            movie_grid_html += movie_html

            # Load the template file
        with open("index_template.html", "r") as f:
            template_content = f.read()

        # Replace the placeholders with actual values
        website_html = template_content.replace("__TEMPLATE_TITLE__", "My Movie List").replace(
            "__TEMPLATE_MOVIE_GRID__", movie_grid_html)

        # Save the website HTML to a file
        with open("index.html", "w") as f:
            f.write(website_html)v"""

    def run(self):
        while True:
            print("Movie App Menu")
            print("1. List movies")
            print("2. Movie statistics")
            print("3. Generate website")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_movie_stats()
            elif choice == "3":
                #self._generate_website()
                print("Not ready yet.")
            elif choice == "4":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")


