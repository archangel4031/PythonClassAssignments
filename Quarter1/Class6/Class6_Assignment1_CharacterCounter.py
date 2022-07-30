# Assignment 1
# For a given string, find the count of each character in a string and print the result

# Get input from user, we will take default if the string provided by user is empty

# Take input from user
checkString = input("Enter your desired string (Leave Empty for default value): ")

if(len(checkString) == 0):
    # Using Lorem Ipsum, because well, why not :)
    checkString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sit amet augue et dui hendrerit placerat. Etiam id odio et."

# Convert to Lower Case
checkString = checkString.lower()

# Print the string for reference
print("String is = ", checkString)

# Declare an empty dictionary, we will populate it with keys that represent characters and vlaues that represent character count
charDict = {}

# Iterate and increment values of keys (aka Characters)
for char in checkString:
    # Check if the key i.e. character already exists, YES then increment the count by one i.e the value against the key
    if charDict.get(char):
        charDict[char] += 1
    else:                           # If key does not exist yet, make a new key and set the count i.e the value to 1
        charDict[char] = 1

# Print the character count in a fancy way :)
for keys, values in charDict.items():
    print(f"Character {keys} occurs {values} times")

# End the program
print("***GoodBye!***")
