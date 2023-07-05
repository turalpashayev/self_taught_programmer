# Replace replaces every occurence of a string with another string
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

# Get index of a string
print("animals".index("m"))

# The in keyword checks if a string is part of another string
print("Cat" in "Cat in the hat.")

# Escaping strings with \
print("She said \"Surely.\"")

# \n is a newline character
print("line1\nline2\nline3")

# Slicing strings 
# [start:stop:step]
fict = ["Tolstoy", "Camus", "Orwell", "Huxley", "Austin"]
print(fict[0:3])

# Example of slicing strings
ivan = "In place of death there was light."
print(ivan[0:17])
