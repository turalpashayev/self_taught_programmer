# Errors and Exceprions
# an error is not syntax error is not an exception

# my_string = "Hello!
# print(my_string)



# print(10/0)

try:
    10/0
except ZeroDivisionError:
    print("Error: You attempted to divide by zero.")