# # Scope in functions

# # variables defined outside of a function are global variables such as x, y, and z in the following example:
# x = 1
# y = 2
# z = 3

# def func_global():
#     print(x)
#     print(y)
#     print(z)

# func_global()

# # variables defined inside of a function are local variables such as x, y, and z in the following example:

# def func_local():
#     x = 1
#     y = 2
#     z = 3

# print(x)
# print(y)
# print(z)

# func_local()

# to write to global variables inside of a function, use the global keyword such as x, y, and z in the following example:
x = 100

def func_global():
    # global x
    print(f'Calling vairbale x before changing it: {x}')
    # x += 1
    print(f'Calling vairbale x after incrementing it by 1: {x}')

func_global()
print(f'Printing vairbale x after calling the function: {x}')


