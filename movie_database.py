""" Movie database module """
# 2015-02-10
# Joseph Urbanski
# MCS 50101

import json
from urllib.request import urlopen

class Movie():
    """ Movie class contains the IMDB ID, the title of the movie, the IMDB
        rating, and the movie's director.
    """
    imdb_id = None
    title = None
    imdb_rating = None
    director = None
    year = None

    def find_highest_rated(filename):
        """ This function reads a csv file, then returns a Movie object with
            the highest IMDB rating.
        """
        movie_list = []

        infile = open(filename, 'r')

        for line in infile:
            currline = line.split(',')
            curr_movie = Movie()

            curr_movie.imdb_id = currline[0]
            curr_movie.title = currline[1]
            curr_movie.director = currline[2]
            curr_movie.imdb_rating = float(currline[3])
            curr_movie.year = currline[4]

            movie_list.append(curr_movie)

        movie_list.sort(key=lambda x: x.imdb_rating, reverse=True)

        return movie_list[0]

    def plot(self):
        """ This function returns the OMDB plot for a given Movie.
        """
        url = 'http://www.omdbapi.com/?i=' + self.imdb_id + '&plot=short&r=json'

        data = urlopen(url).read().decode('utf8')
        result = json.loads(data)

        return result['Plot']
