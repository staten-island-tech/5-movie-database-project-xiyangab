import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def movie(m):
    for a in data:
        if a['title'] in m:
            print(a['title'])
            print(a['genres'])
movie('M3GAN')