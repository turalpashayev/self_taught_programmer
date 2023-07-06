# Format method for strings
# print("XSOAR ticket number is {}".format('1234567'))

# You can use the format method to insert values into a string
ticket_number = 1234567
l1_analyst = 'Abesh'
l2_analyst = 'Colin'
# print("XSOAR ticket number is: {} L1 Analyst is: {} L2 Analyst is: {}".format(ticket_number, l1_analyst, l2_analyst))
# print(f"XSOAR ticket number is: {ticket_number} L1 Analyst is: {l1_analyst} L2 Analyst is: {l2_analyst}")

# split method splits a string into a list of strings
greeting = "Hello World"
# print(greeting.split())

email_address = 'abc@gmail.com'
extracted_domain = email_address.split('@')
# print(extracted_domain[1])
      
# join method joins a list of strings into a single string
first_three = "abc"
result = " ".join(first_three)
# print(result)

# Concantinate list items in one string
words = ["The", "fox", "jumped", "over", "the", "fence."]
one = ", ".join(words)
# print(one)

# strip method removes whitespace from the beginning and end of a string
s = "    The    "
s = s.strip()
# print(s

# strip method removes characters from the beginning and end of a string
s = 'abcHelloabc'
print(s.strip('abch'))