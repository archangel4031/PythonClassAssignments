# Assignment 3
# Get an input from the user and check if it is a Palindrome or not

# Import Math Libraries
from math import floor

False

# Global flag to use in print statements
FLAG = False

# Creating functions for readibility
# Function for checking if input is of Odd length
def checkOddLength(checkString):
    global FLAG
    for i in range(midpoint+1):
        if(checkString[midpoint+i] == checkString[midpoint-i]):
            continue
        else:
            print("String is NOT a Palindrome")
            FLAG = True
            break
    if(not FLAG):
        print("String is a Palindrome")

# Function for checking if input is of Even length
def checkEvenLength(checkString):
    global FLAG
    for i in range(midpoint):
        if(checkString[midpoint + i] == checkString[midpoint - i-1]):
            continue
        else:
            print("String is NOT a Palindrome")
            FLAG = True
            break
    if(not FLAG):
        print("String is a Palindrome")


# Get input from user, provide default string if input is empty
# Get the input
checkString = input("Enter the String to check (Leave empty for default): ")

# Use default if input is empty
if(len(checkString) == 0):
    # checkString = "123454321"
    checkString = "12344321"

# Print the string
print("String is: ", checkString)

# Find Midpoint
midpoint = len(checkString) / 2
# Convert to Integer, lower / floor value
midpoint = floor(midpoint)

# Call appropriate function to decide how to check Palindrome
if (midpoint == len(checkString) / 2):
    print("Even Length String")
    checkEvenLength(checkString)
else:
    print("Odd Length String")
    checkOddLength(checkString)


# End the program
print("***GoodBye!***")
