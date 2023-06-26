# You can store container in other container
# You can store list in list
lists = []
rap = ["Kanye West", "Jay Z", "Eminem", "Nas"]
rock = ["Bob Dylan", "The Beatles", "Led Zeppelin"]
djs = ["Zeds Dead", "Tiesto"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
# print(lists)

# You can store tuple in list
locations = []
la = (34.0522, 188.2437) # Los Angeles
chicago = (41.8781, 87.6298) # Chicago
locations.append(la)
locations.append(chicago)
# print(locations)

# You can store dictionary in list
bday = {"Hemingway": "7.21.1899", "Fitzgerald": "9.24.1896"}
my_list = [bday]
# print(my_list)

# A list, tuple or dictionary can be a value in a dictionary
ny = {"location": (40.7128, 74.0059), "celebs": ["W. Allen", "Jay Z", "K. Bacon"], "facts": {"state": "NY", "country": "America"}}
# print(ny)