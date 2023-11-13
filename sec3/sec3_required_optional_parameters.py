# Required and optional parameters
# Required parameters must be specified in the same order as they are defined.

# def my_function1(fname, lname):
#   print(fname + " " + lname)

# my_function1("Emil", "Refsnes")

# Optional parameters are often used for keyword arguments, which are name-value pairs.
def my_function2(country = "Norway"):
  print("I am from " + country)
  
my_function2("Sweden")