import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def year(a):
    for y in data:
        if y['year'] > a:
            print(y['title'])
year(2022)