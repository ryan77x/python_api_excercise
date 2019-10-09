# This Python script gets movie details from http://www.omdbapi.com API and then store them into a local file.
# Author: Ryan Liang

import requests

omdb = "http://www.omdbapi.com"
api_key = "dummy"
fileName = "movies_details.txt"

def getMovieDetail(movieID):
    url = omdb + "/?i=" + movieID + "&apikey=" + api_key
    try:
        response = requests.get(url)
        if response.status_code == 200:
            movieData = response.json()
            saveToFile(movieData)
        else:
            print("Unable to query the request data at this time")
    except Exception as error:
        print(error)

def saveToFile(movieData):
    try:
        with open(fileName, "a") as file:
            keys = ["Title", "Released", "Runtime", "Genre", "imdbRating", "BoxOffice", "Poster", "Plot"]
            for key in keys:
                file.write(key + ": " + movieData[key] + "\n")
            file.write("\n")
    except IOError as error:        
                print(error)

movies = ["tt0086190", "tt0089880", "tt0088247", "tt0372784", "tt0080684"] 
for movie in movies:
    getMovieDetail(movie)