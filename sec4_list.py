# We can create lists with two different ways:
fruit = list()
fruit = []

# Creating lists with items already in it
fruits = ['apple', 'orange', 'banana']
# print(fruits)

# Using append method to add items to the list
fruits.append('pear')
fruits.append('kiwi')
# print(fruits)

# Lists are iterable objects
# It means items has indexes

fruit = ['apple', 'orange', 'banana']
# print(fruit[2])

# Lists are mutable objects
# It means we can change the items in the list
fruit[0] = 'pear'
# print(fruit)

# Removing items from the list
colors = ['red', 'green', 'blue']
# print(colors)
colors.pop(1)
print(colors)

# using in operator to check if an item is in the list
if 'red' in colors:
    pass
    # print('red is in the list')

# Using addition to concatenate lists
colors1 = ['black','white','gray']
colors2 = ['red', 'green', 'blue']
colors_all = colors1 + colors2
# print(colors_all)
