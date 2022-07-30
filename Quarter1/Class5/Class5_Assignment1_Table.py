# Assignment 1
# Take a number from user and print Multiplication Table

# Gather input from user
numUser = int(input("Enter a number to generate table: "))

# Generate Table
print("===============")
for i in range(1, 11):
    print(f"{numUser} x {i} = ", numUser*i)
print("===============")

# End the program
print("***GoodBye!***")
