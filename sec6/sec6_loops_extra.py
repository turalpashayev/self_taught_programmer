# using built-in range() function
for i in range(101):
    pass
    # print(i)

# using while loop
x = 10
while x > 0:
    # print(x)
    x -= 1

# using break statement
for i in range(1, 11):
    if i == 8:
        break
    # print(i)

# using continue statement
for i in range(1, 5):
    if i == 3:
        continue
    # print(i)

# using nested loops
lis1 = [1, 2, 3, 4]
lis2 = [5, 6, 7, 8]
added = []
for i in lis1:
    for j in lis2:
        added.append(i + j)
# print(len(added))


numbers = [1,2,3,4,5,6,7,8,9,10]

valid_user_input = True
while valid_user_input:
    user_input = input('Please enter number form 1 to 10:')
    if int(user_input) in numbers:
        valid_user_input = False
    print("Please enter number from 1 to 10. Entered number is not in the range")