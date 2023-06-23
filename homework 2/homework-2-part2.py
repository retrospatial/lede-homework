# Florina Sutanto
# June 7, 2023
# Homework 2, Part 2

# LISTS

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ["Indonesia", "Singapore", "Canada", "Monaco", "Japan", "Bahrain", "Azerbaijan"]

# 2) Using a for loop, print each element of the list
for country in countries:
    print(country)

# 3) Sort the list permanently.
countries = sorted(countries)
print(countries)

# 4) Display the first element of the list.
print(countries[0])

# 5) Display the second-to-last element of the list.
print(countries[-2])

# 6) Delete one of the countries from the list using its name.
list.remove(countries, 'Bahrain')
print(countries)

# 7) Using a for loop, print each country's name in all caps.
for country in countries:
    print(country.upper())

# DICTIONARIES

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. 
# Taken from https://en.wikipedia.org/wiki/List_of_individual_trees
tree = {
    'name': 'Caesarsboom',
    'species': 'Taxus baccata',
    'age': 2000,
    'location_name': 'Lo, Lo-Reninge, Belgium',
    'latitude': 50.9807,
    'longitude': 2.7490
}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(tree['name'], "is a", tree['age'], "year old tree that is in", tree['location_name'])

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
nyc_lat = 40.7128

if tree['latitude']>nyc_lat:
    print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC."),
elif tree['latitude']<nyc_lat:
    print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC."),
else:
    print("The tree", tree['name'], "in", tree['location_name'], "is on the same latitude as NYC.")

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
age = input("How old are you?")
age = int(age)
age_diff = abs(tree['age']-age)

if age>tree['age']:
    print("You are", age_diff, "years older than", tree['name'])
else:
    print(tree['name'], "was", age_diff, "years old when you were born.")

# LISTS OF DICTIONARIES

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).
places = [
    {'name': 'Moscow',
    'latitude': 55.7558,
    'longitude': 37.6173},
    {'name': 'Tehran',
    'latitude': 35.7219,
    'longitude': 51.3347},
    {'name': 'Falkland Islands',
    'latitude': -51.7963,
    'longitude': -59.5236},
    {'name': 'Seoul',
    'latitude': 37.5519,
    'longitude': 126.9918},
    {'name': 'Santiago',
    'latitude': -33.4489,
    'longitude': -70.6693}
]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
for place in places:
    if place['latitude']>0:
        print(place['name'], "is above the equator."),
    elif place['latitude']<0:
        print(place['name'], "is below the equator."),
    else:
        print(place['name'], "is on the equator."),
    if place['name'] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the wild Antarctic zone.")

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for place in places:
    if place['latitude']>tree['latitude']:
        print(place['name'], "is north of", tree['name']),
    if place['latitude']<tree['latitude']:
        print(place['name'], "is south of", tree['name'])

# CLass

art_pieces = [
    {'title': 'Gold Star', 'year':1805},
    {'title': 'Blunderbuss', 'year':1800},
    {'title': 'Chairlirft', 'year':1976},
    {'title': 'Rancor', 'year':2002},
]

for art in art_pieces:
    print(art['title'])

murders = {
    'Albany': 23,
    'Kings': 10,
    'Rochester': 7,
    'Yonkers': 9
}

print(sum(murders.values()))