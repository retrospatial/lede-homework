# Florina Sutanto
# June 6, 2023
# Homework 1

# comment: ctrl+k+c, or ctrl+/

birth_year = int(input('Hi! What year were you born?'))

# REVISION
# birth_year = (input('Hi! What year were you born?'))
# birth_year = int(birth_year)
# this_year = 2023
# age = this_year - birth_year
# print(age)

while birth_year>2023:
    print("That's in the future! Please enter your real birth year.")
    birth_year = int(input('Hi! What year were you born?'))

# How old the user is
age = 2023-birth_year
print("You are", age, "years old")

# How many times the user's heart has beaten
heart_beat = round(age*35)
print("Your heart has beaten", heart_beat, "million times in your lifetime.")

# REVISION - USE F STRINGS
# heart_beat = (age*35000000)
# print(f"Your heart has beaten about {heart_beat:,} times in your lifetime")

# How many times a blue whale's heart has beaten in that time
whale_heart_beat = round(age*17.3)
print("A blue whale's heart has beaten", whale_heart_beat, "million times in your lifetime.")

# How many times a rabbit's heart has beaten in that time
rabbit_heart_beat = round(age*78.8)
print("A rabbit's heart has beaten", rabbit_heart_beat, "million times in your lifetime.")

# How old they are in Venus years
venus_age = round(age/0.615)
print("You are", venus_age, "Venus years old")

# How old they are in Neptune years
neptune_age = round(age/165, ndigits=2)
print("You are", neptune_age, "Neptune years old")

# Whether they are the same age as you, older or younger
# If older or younger, how many years difference
my_age = 21
if age == my_age:
    print("We're the same age!")
elif age<my_age:
    ageDiff=my_age-age
    print("You're younger than me by", ageDiff, "year(s)")
else:
    ageDiff=age-my_age
    print("You're older than me by", ageDiff, "year(s)")

# If they were born in an even or odd year
even_odd = birth_year%2
if even_odd == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
demPress = 0
if birth_year<=1960:
    print("Sorry, I don't know how many presidents from the Democratic party there have been before 1960.")
elif birth_year>=2017:
    demPress = demPress + 1
    print("There has/have been", demPress, "president(s) from the Democratic party since you were born.")
    print("Those were: Joe Biden.")
elif birth_year>=2001:
    demPress = demPress + 2
    print("There has/have been", demPress, "president(s) from the Democratic party since you were born.")
    print("Those were: Joe Biden and Barack Obama.")
elif birth_year>=1981:
    demPress = demPress + 3
    print("There has/have been", demPress, "president(s) from the Democratic party since you were born.")
    print("Those were: Joe Biden, Barack Obama, and Bill Clinton.")
elif birth_year>=1969:
    demPress = demPress + 4
    print("There has/have been", demPress, "president(s) from the Democratic party since you were born.")
    print("Those were: Joe Biden, Barack Obama, Bill Clinton, and Jimmy Carter.")
elif birth_year>=1963:
    demPress = demPress + 5
    print("There has/have been", demPress, "president(s) from the Democratic party since you were born.")
    print("Those were: Joe Biden, Barack Obama, Bill Clinton, Jimmy Carter, and Lyndon B. Johnson.")
elif birth_year>=1960:
    demPress = demPress + 6
    print("There has/have been", demPress, "president(s) from the Democratic party since you were born.")
    print("Those were: Joe Biden, Barack Obama, Bill Clinton, Jimmy Carter, Lyndon B. Johnson, and John F. Kennedy.")

# REVISION
dems = [1961,1963,1977,1992,2008,2020]
count = 0
for dem in dems:
    if birth_year <= dem:
        count = count + 1
print("You have lived through",count,"Democratic Presidents")

# Which US President was in office when they were born (1960 onwards)
presidents = [
    "Dwight D. Eisenhower",
    "John F. Kennedy",
    "Lyndon B. Johnson",
    "Richard Nixon",
    "Gerald Ford",
    "Jimmy Carter",
    "Ronald Reagan",
    "George H.W. Bush",
    "Bill Clinton",
    "George W. Bush",
    "Barack Obama",
    "Donald Trump",
    "Joe Biden"
]

if birth_year<1960:
    print("Sorry, I don't know which president was in office before 1960.")
elif birth_year>=1960 and birth_year<1961:
    print("The president in office when you were born is", presidents[0])
elif birth_year>=1961 and birth_year<1963:
    print("The president in office when you were born is", presidents[1])
elif birth_year>=1963 and birth_year<1969:
    print("The president in office when you were born is", presidents[2])
elif birth_year>=1969 and birth_year<1974:
    print("The president in office when you were born is", presidents[3])
elif birth_year>=1974 and birth_year<1977:
    print("The president in office when you were born is", presidents[4])
elif birth_year>=1977 and birth_year<1981:
    print("The president in office when you were born is", presidents[5])
elif birth_year>=1981 and birth_year<1989:
    print("The president in office when you were born is", presidents[6])
elif birth_year>=1989 and birth_year<1993:
    print("The president in office when you were born is", presidents[7])
elif birth_year>=1993 and birth_year<2001:
    print("The president in office when you were born is", presidents[8])
elif birth_year>=2001 and birth_year<2009:
    print("The president in office when you were born is", presidents[9])
elif birth_year>=2009 and birth_year<2017:
    print("The president in office when you were born is", presidents[10])
elif birth_year>=2017 and birth_year<2021:
    print("The president in office when you were born is", presidents[11])
elif birth_year>=2021 and birth_year<=2023:
    print("The president in office when you were born is", presidents[12])
