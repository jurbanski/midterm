# MPCS 50101 Winter 2015 Midterm
# ---------------------------------------------------------
#
# FOLLOW THE INSTRUCTIONS IN README.MD!
#
# Any changes to this file will be ignored.
# Hints are provided at the bottom of this file.
#
# ---------------------------------------------------------


from movie_database import Movie
best_movie = Movie.find_highest_rated('imdb_top250.csv')

assert type(best_movie) is Movie
assert best_movie.title == "The Shawshank Redemption"
assert best_movie.imdb_rating == 9.3
assert best_movie.director == 'Frank Darabont'
assert "imprisoned" in best_movie.plot()







#####

print("* All assertions passed. Nice work!")
print("* Remember to sync your code to GitHub and ensure that it's there!")
print("* Have a nice week!")




### HINTS:
### -------
### 1. Before starting to code, run this file and read the error message.
### 2. Do the Simplest Thing That Can Possibly Work™ to resolve the error.
### 3. Run the file again. Use Error-Driven Development™ until all assertions pass.
### 4. You can open a CSV for reading with proper UTF-8 encoding like this:
###
###       with open("filename.csv", encoding='utf-8') as f:




