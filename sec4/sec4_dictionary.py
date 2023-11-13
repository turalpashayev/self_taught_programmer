# We can create dictioneries with two different ways:
my_dict = dict()
my_dict = {}

# Creating dictioneries with items already in it
fruits = {'apple': 'red', 'banana': 'yellow', 'pear': 'green'}

for key, value in fruits.items():
    print(f'Key is: {key} Value is {value}')

# Adding value to the dictionary
fruits['pear'] = 'green'
# print(fruits)

# Looking up for value in the dictionary
# print(fruits['pear'])

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