import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def year(a,b):
    for y in data:
        if y['year'] > a and y['year'] < b:
            print(y['title'])
year(2022,2024)