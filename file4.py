import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def year(d):
    for y in data:
        if y['year'] == d:
            print(y['title'])
year(2023)