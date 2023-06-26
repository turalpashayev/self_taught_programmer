# We can create dictioneries with two different ways:
my_dict = dict()
my_dict = {}

# Creating dictioneries with items already in it
fruits = {'apple': 'red', 'banana': 'yellow'}

# Adding value to the dictionary
fruits['pear'] = 'green'

# Looking up for value in the dictionary
fruits['pear']

# Checking if key is in the dictionary using in operator
# We can not check if value is in the dictionary    

if 'apple' in fruits:
    pass
    # print('apple is in the dictionary')

# Change value in the dictionary
fruits['apple'] = 'green'
# print(fruits)

# Delete item from the dictionary
del fruits['banana']
# print(fruits)