# What is difference between '==' and 'is'?
# '==' checks for equality, 'is' checks for identity
# For example:

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# check location of a and b
print(id(a))
print(id(b))

print(id(a) == id(b))