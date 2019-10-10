# This Python script gets movie details from http://www.omdbapi.com API and then stores them into a local file.
# Author: Ryan Liang

import requests

omdb = "http://www.omdbapi.com"
api_key = "dummy"
file_name = "movies_details.txt"

def get_movie_detail(movie_ID):
    url = omdb + "/?i=" + movie_ID + "&apikey=" + api_key
    try:
        response = requests.get(url)
        movie_data = response.json()
        if response.status_code == 200 and movie_data["Response"] == "True":
            return movie_data
        else:
            print("Unable to query the requested data at this time or invalid movie ID / API key")
            return False
    except Exception as error:
        print(error)
        return False

def save_to_file(movie_data):
    try:
        with open(file_name, "a") as file:
            keys = ["Title", "Released", "Runtime", "Genre", "imdbRating", "BoxOffice", "Poster", "Plot"]
            for key in keys:
                file.write(key + ": " + movie_data[key] + "\n")
            file.write("\n")
            return True
    except Exception as error:  
        print(error)
        return False 

movies = ["tt0088247", "tt0086190", "tt0089880", "tt0372784", "tt0080684"]
for movie in movies:
    movie_data = get_movie_detail(movie)
    if movie_data != False:
        save_to_file(movie_data)
