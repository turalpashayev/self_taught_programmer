# We can create lists with two different ways:
fruit = list()
fruit = []

# Creating lists with items already in it
fruits = ['apple', 'orange', 'banana']

# Using append method to add items to the list
fruits.append('pear')
fruits.append('kiwi')
print(fruits)

# Lists are iterable objects
# It means items has indexes

fruit = ['apple', 'orange', 'banana']
print(fruit[0])

# Lists are mutable objects
# It means we can change the items in the list
fruit[0] = 'pear'

# Removing items from the list
colors = ['red', 'green', 'blue']
colors.pop()
print(colors)

# using in operator to check if an item is in the list
if 'red' in colors:
    print('red is in the list')

# Using addition to concatenate lists
colors1 = ['black','white','gray']
colors2 = ['red', 'green', 'blue']
colors_all = colors1 + colors2
print(colors_all)
