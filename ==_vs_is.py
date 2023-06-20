# What is difference between '==' and 'is'?
# '==' checks for equality, 'is' checks for identity
# For example:

# a = 1
# b = 1
# print(a ==  b)  # True
# print(a is b)  # False

# # check location of a and b
# # print(id(a))
# # print(id(b))

# # print(id(a) == id(b))

# data = {
#     'name': 'Alice',
#     'age': None
# }

x = 10
y = 20
max = x if x > y else x
print(max)
