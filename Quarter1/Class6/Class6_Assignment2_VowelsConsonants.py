# Assignment 2
# For a given string, find the count of Vowels and Consonants and print the result

# Declare list of Vowels, rest will automatically be consonants
vowelsList = ["a", "e", "i", "o", "u"]

# Declare variables for Counters
vowelsCount = 0
consonantsCount = 0

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

# Iterate through the string character-by-character and check if it exists in vowelsList
for char in checkString:
    if(char in vowelsList):         # If in vowelsList, increment vowelsCount
        vowelsCount += 1
    elif(char == " "):              # Skip spaces for counting
        continue
    else:                           # All other characters would be Consonants
        consonantsCount += 1

# Print the result
print("Total Vowels are ", vowelsCount)
print("Total Consonants are ", consonantsCount)

# End the program
print("***GoodBye!***")
