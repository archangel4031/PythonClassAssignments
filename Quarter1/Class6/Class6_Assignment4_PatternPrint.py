# Assignment 4
# Print a Pattern in the following form
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# Get input from user
userNum = int(input("Enter a Number: "))
print()


# Nested Loop to print the pattern
for i in range(1, userNum + 1):
    for j in range(1, (userNum - i) + 2):
        print(j, end=" ")
    print()


# End the program
print("***GoodBye!***")
