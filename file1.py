import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# file one
""" for t in data:
    print(t['title']) """

#file two
""" def year(a):
    for y in data:
        if y['year'] > a:
            print(y['title'])
year(2022) """

#file three
""" def year(a,b):
    for y in data:
        if y['year'] > a and y['year'] < b:
            print(y['title'])
year(2022,2024) """

#file four
""" def year(d):
    for y in data:
        if y['year'] == d:
            print(y['title'])
year(2023) """

#file five
""" def movie(m):
    for a in data:
        if a['title'] == m:
            print(a['title'])
movie('Migration') """

#file six
def genre(g):
    for a in data:
        if g in a['genres']:
            print(a['title'])
genre("Thriller")