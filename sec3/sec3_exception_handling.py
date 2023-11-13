# Exception Handling

# # code block without exception handling
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# a = int(a)
# b = int(b)
# print(a / b)

# # code block with exception handling
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# a = int(a)
# b = int(b)

# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("b cannot be zero")

# # more code block with exception handling
a = input("Enter a number: ")  
b = input("Enter another number: ")


try:
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input(s)")