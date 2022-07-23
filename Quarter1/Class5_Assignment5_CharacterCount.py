# Assignment 5
# For a given string, get a character from user and find its number of occurrence in the string

# Define the string, we can take an input from the user but to keep it simple, using pre-defined string
# Using Lorem Ipsum, because well, why not :)
checkString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sit amet augue et dui hendrerit placerat. Etiam id odio et."

# Print the string for reference
print("String is = ", checkString)

# Gather input from user
userChar = input("Enter a character to check in the string = ")

# Initialize a counter
count = 0

# Iterate through the string
for i in checkString.lower():
    if userChar == i:
        count += 1

# Print the result
print("Occurences of Character '", userChar, "' are = ", count)

# End the program
print("***GoodBye!***")
