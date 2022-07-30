# Assignment 2
# Generate 100 random numbers between 10 and 90 and store them in a sepearate array
# a. Find their sum and average
# b. Find maximum number
# c. Find minimum number
# d. Check how many numbers are greater than 40 (using continue command)

# Import Library
import random

# Define control variables, they are not needed if values are already decided
# These will take memory space and should be avoided if possible
MIN_RANGE = 10
MAX_RANGE = 90
LIST_LENGTH = 100

# Declare a list to store random numbers
randomList = []

# Generate Random Number and store in the list
for i in range(LIST_LENGTH):
    randomList.append(random.randint(MIN_RANGE, MAX_RANGE))

print("Random List")
print(randomList)       # Print the list for reference

# **************************************************************************************
# Task 1: Calculate Sum and Averages
print("\n***Task 1***\n")

# Declare variable to store values
sum = 0
avg = 0

# Calcualte Sum
for i in randomList:
    sum += i

# Calcualte Average
avg = sum / len(randomList)

# Print the values
print("Sum of list is = ", sum)
print("Average of Numbers is = ", avg)

# **************************************************************************************
# Task 2: Find Max Number
print("\n***Task 2***\n")

# This is the easy way to do it :D
print("[EASY] Max Value in List is = ", max(randomList))

# This is the assignment way to do it :)
# Assume that the first element is greatest, then use loop to update its value
maxVal = randomList[0]

for i in randomList:
    if(i > maxVal):         # check if element is greater than maxVal
        maxVal = i          # if YES then make it the maxVal

# Print the value after loop completes
print("[HARD] Max Value in List is = ", maxVal)

# **************************************************************************************
# Task 3: Find Min Number
print("\n***Task 3***\n")

# Again going for easy way
print("[EASY] Min Value in List is = ", min(randomList))

# And the assignmet way to do it
# Assume that tht first element is smallest, then update its value using loop
minVal = randomList[0]

for i in randomList:
    if(i < minVal):         # Check if element is less than minVal
        minVal = i          # If YES then make it minVal

# Print the value after loop completes
print("[HARD] Min Value in List is = ", minVal)

# **************************************************************************************
# Task 4: Calculate number greater than 40 and print that list
print("\n***Task 4***\n")

# Declare an empty list to store results
greaterThan40 = []

# Iterate through the list and store the result
for i in randomList:
    if(i < 40):
        continue            # exit out of current iteration if element is less than 40
    greaterThan40.append(i)  # If not then store the number in the list

print("List of elements greater than 40 = ", greaterThan40)

# End the program
print("***GoodBye!***")