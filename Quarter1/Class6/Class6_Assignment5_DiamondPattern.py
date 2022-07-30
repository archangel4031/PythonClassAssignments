# Assignment 5
# Print a Pattern in the following form
#      5
#     4 4
#    3   3
#   2     2
#  1       1
#   2     2
#    3   3
#     4 4
#      5



# Get input from user
userNum = int(input("Enter a Number = "))
print()

# Nested Loop to print the Pattern, using dot "." to visualize spaces

# Print Top Pattern
for i in range(userNum, 0, -1):
    for j in range(i):
        print(end=".")
    print(i,end="")
    for k in range(userNum, i, -1):
        print(end=".")
        print(end=".")
    if(not(i == userNum)):    
        print(i,end="")
    print()

# Print Bottom Pattern
for i in range(1, userNum+1):
    for j in range(i):
        print(end=".")
    print(i,end="")
    for k in range(i, userNum):
        print(end=".")
        print(end=".")
    if(not(i == userNum)):    
        print(i,end="")
    print()




# End the program
print("***GoodBye!***")