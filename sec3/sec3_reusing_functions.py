# Function can encapsulate functionality you want to reuse

def print_even_or_odd():
    input_string = input("Type number: ")
    input_number = int(input_string)
    if input_number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Input first number
print_even_or_odd()

# Input second number
print_even_or_odd()

# Input third number
print_even_or_odd()
