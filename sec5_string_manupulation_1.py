# Format method for strings
print("XSOAR ticket number is {}".format('1234567'))

# You can use the format method to insert values into a string
ticket_number = 1234567
print("XSOAR ticket number is: {}".format(ticket_number))

# split method splits a string into a list of strings
greeting = "Hello World"
print(greeting.split())
      
# join method joins a list of strings into a single string
first_three = "abc"
result = "+".join(first_three)
print(result)

words = ["The", "fox", "jumped", "over", "the", "fence."]
one = "".join(words)
print(one)

# strip method removes whitespace from the beginning and end of a string
s = "    The    "
s = s.strip()
print(s)