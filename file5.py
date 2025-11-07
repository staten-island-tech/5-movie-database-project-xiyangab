import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def movie():
    m = input("what move do you like")
    b = 0
    for a in data:
        if m.lower() in a['title'].lower():
            print(a['title'])
            b += 1
    if b == 0:
        print("no results")
movie()