# We can create tuples with two different ways:
my_tuple = tuple()
my_tuple = ()

# Random tuple
random = ('Micheal', 10, True)

# We can get item from tuple by index referencing the item index
print(random[1])

# We can check if item is in tuple using in operator
if 'Micheal' in random:
    print('Micheal is in the tuple')

# Tuple versus number in parentheses
# this is tuple
('hello',)

# this is not tuple
(9)

# We can not change tuple once it is created
random[0] = 'John'

