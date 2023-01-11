movie = {'name': 'Burning', 'type': 'movie', 'year': 2018}

try:
    rating = movie['rating']
except KeyError:
    rating = 0

print(rating)
print(movie.get('rating'))
