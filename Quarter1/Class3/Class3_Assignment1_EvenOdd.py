# Assignment 1
# This program takes a number as input from the user and tells if it is Even or Odd

# Take the Input from the user, generally we would have some sort of input validation here
num1 = int(input("Enter a number: "))

# Calculate the Mod to determine if it is EVEN or ODD
result = num1 % 2

# Check if it is even or odd (EVEN = 0, ODD = 1)
if result == 0:
    print("The Number is an EVEN Number")
else:
    print("The Number is an ODD Number")

# End the program
print("*** GOODBYE! ***")
