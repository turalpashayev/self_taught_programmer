# What is difference between '==' and 'is'?
# '==' checks for equality, 'is' checks for identity
# For example:

a = 999999999999999999999999999999999999999999999999999.99999999999999999999999999999
b = 999999999999999999999999999999999999999999999999999.99999999999999999999999999999
print(a ==  b)  # True
print(a is b)  # False

# check location of a and b
# print(id(a))
# print(id(b))

# print(id(a) == id(b))