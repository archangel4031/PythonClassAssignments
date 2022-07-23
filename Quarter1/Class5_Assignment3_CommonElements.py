# Assignment 3
# Given two Lists, find the common elements and print the list

# Define the lists (manual definition to keep things simple)
listFirst = [1, 2, 3, 4, 5, 6]
listSecond = [3, 4, 5, 6, 7, 8]

# Declare list to store common elements
commonElements = []

# Iterate through the list and store results
# Use nested for loops to find common elements and append to new list
for i in listFirst:
    for j in listSecond:
        if i == j:
            commonElements.append(j)

# Print the result
print("Common Elements are = ", commonElements)

# Another interesting way to do the same task is (Thank you Google!)
common_list = [element for element in listFirst if element in listSecond]

# Print the result
print("Common Elements are = ", common_list)

# End the program
print("***GoodBye!***")
