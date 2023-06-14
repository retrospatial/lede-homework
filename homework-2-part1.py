# Florina Sutanto
# June 7, 2023
# Homework 2, Part 1

# LISTS 

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
list = [22, 90, 0, -10, 3, 22, 48]

# Display the number of elements in the list.
print(len(list))

# Display the 4th element of this list.
print(list[3])

# Display the sum of the 2nd and 4th element of the list.
print(list[1]+list[3])

# Display the 2nd-largest value in the list.
print(sorted(list)[-2])

# Display the last element of the original unsorted list
print(list[-1])

# Display the sum of all of the numbers divided by two.
print(sum(list)/2)

# Print whether the median or the mean of the numbers is higher
sorted_list = sorted(list)
# print(sortedList)
n = int((len(list)+1)/2)
median = sorted_list[n]
print(median)

mean = int(sum(list)/len(list))
print(mean)

if median>mean:
    print("The median of this list is larger than the mean"),
elif median<mean:
    print("The mean of this list is larger than the median"),
else:
    print("They mean and median are equal!")

# # checking
# import statistics 
# if statistics.mean(list) > statistics.median(sorted(list)):
#     print("The mean of this list is larger than the median")
# else:
#     print("The median of this list is larger than the mean")



# DICTIONARIES

# Define a dictionary called movie that works with the following code.
# On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
movie = {
    'title': 'Whip It',
    'year': 2009,
    'director': 'Drew Barrymore'
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie['budget'] = 15000000
movie['revenue' ]= 16600000

print(movie['revenue']-movie['budget'])

# If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

if movie['revenue']<movie['budget']:
    print("That was a bad investment")
elif movie['revenue']>movie['budget']*5:
    print("That was a great investment")
else:
    print("That was an okay investment")

# Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
nyc_boroughs = {
    'Manhattan': 1600000,
    'Brooklyn': 2600000,
    'Bronx': 1400000,
    'Queens': 2300000,
    'Staten Island': 470000
}

# Display the population of Brooklyn.
print('Brooklyn has a population of', nyc_boroughs["Brooklyn"], 'people.')

# Display the combined population of all five boroughs.
sum_population = sum(nyc_boroughs.values())
print('The combined population of all five boroughs is', sum_population, 'people.')

# Display what percent of NYC's population lives in Manhattan.
manhattan = (nyc_boroughs['Manhattan']/sum_population)*100
manhattan = str(round(manhattan, ndigits= 2))
print(manhattan + "% of New Yorkers live in Manhattan")