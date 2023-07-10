# for loop used to iterate over a sequence (list, tuple, string) or other iterable objects
name = "Python"
for letter in name:
    print(letter)

# for loop with list
shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

# for loop with tuple
coms = ("A. Development", "Friends", "Always Sunny")
for show in coms:
    print(show)

# for loop with dictionary
people = {"G. Bluth II": "A. Development", "Barney": "HIMYM", "Dennis": "Always Sunny"}
for character in people:
    print(character)

# you can use the .items() method to access both keys and values in a dictionary

# you can use for loops to change the items in a mutable iterable
tv = ["Got", "Narcos", "Vice"]
# print(tv)
i = 0
for shows in tv:
    shows = shows.upper()
    tv[i] = shows
    i += 1
# print(tv)

# you can combine two lists using the for loop
tv = ["Got", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []
for show in tv:
    all_shows.append(show)

for show in coms:
    all_shows.append(show)

# print(all_shows)

# using extend method to combine two lists
tv = ["Got", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
tv.append(coms)
print(tv)