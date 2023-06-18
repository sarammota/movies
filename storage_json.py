from movies.istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: {self.file_path} file not found.")
            return {}

    def add_movie(self, title, year, rating, poster):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[title] = {
            "rating": rating,
            "year": year,
            "poster": poster
        }

        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def delete_movie(self, title):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.file_path} file not found.")
            return

        if title in data:
            del data[title]
            with open(self.file_path, 'w') as file:
                json.dump(data, file)
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found in the database.")

    def update_movie(self, title, notes):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.file_path} file not found.")
            return

        if title in data:
            data[title]['notes'] = notes
            with open(self.file_path, 'w') as file:
                json.dump(data, file)
            print(f"Movie '{title}' notes updated successfully.")
        else:
            print(f"Movie '{title}' not found in the database.")








