#!/usr/bin/env python
"""
dicts.py

Dictionaries
============================================================ 
In this section, write some functions which build and 
manipulate python dictionaries.
"""

def freq(data):
    frequency = dict()
    for x in range(0,len(data)):
        if data[x] not in frequency:
            frequency[data[x]] = 1
        else:
            frequency[data[x]] += 1
    return frequency




movies = {}

def score(title, value):
    if title not in movies:
        movies[title] = [value]
    else:
        movies[title].append(value)
        
    


def avg_score(title):
    "return the average score for a given movie"
    if title in movies:
        to_sum = movies[title][:]
    score = 0
    score = float(score)
    for x in range (0,len(to_sum)):
        score += to_sum[x]
    score = score/len(to_sum)
    return score
    


# 3. parse_csv (Advanced)
#        Takes an input string and spits back a list of comma
#        separated values (csv) entries.  Hint, check the zip
#        and dict functions.
#
#        The point of this is to create your own parser, not to
#        use pythons builtin 'csv' library.
#
#           >>> csv = """
#           name,age,email
#           Foo, 24, foo@example.com
#           Bar ,22 ,bar@example.com
#           Baz, 20 , baz@gmail.com
#           """
#           >>> parse_csv(csv)
#           [ { "name": "Foo", "age": "24", "email": "foo@example.com" },
#             { "name": "Bar", "age": "22", "email": "bar@example.com" },
#             { "name": "Baz", "age": "20", "email": "baz@example.com" } ]            

def parse_csv(data):
    "parses a csv file into a list of dictionaries"

