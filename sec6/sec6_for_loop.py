# for loop used to iterate over a sequence (list, tuple, string) or other iterable objects
name = "Python"
for letter in name:
    pass
    # print(letter)

# for loop with list
shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    pass
    # print(show)

# for loop with tuple
coms = ("A. Development", "Friends", "Always Sunny")
for show in coms:
    pass
    # print(show)

# for loop with dictionary
people = {"G. Bluth II": "A. Development", "Barney": "HIMYM", "Dennis": "Always Sunny"}
for character in people:
    pass
    # print(character)

# for key, value in people.items():
#     print(f'Key is: {key}, Value is: {value}')
# you can use the .items() method to access both keys and values in a dictionary

# you can use for loops to change the items in a mutable iterable
tv = ["Got", "Narcos", "Vice"]
# print(tv)
for index, shows in enumerate(tv):
    shows = shows.upper()
    tv[index] = shows
# print(tv)

# you can combine two lists using the for loop
tv = ["Got", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = tv + coms


print(all_shows)
