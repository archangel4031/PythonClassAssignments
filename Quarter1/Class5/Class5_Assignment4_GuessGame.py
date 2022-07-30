# Assignment 4
# Generate a Random Number and give three tries to user to guess the number

# Import Library
import random

# Define the range for random number
MIN_VALUE = 0
MAX_VALUE = 10
TRIES = 3

# This is not needed, a simple check of userGuess with randomNumber would suffice and save memory
# FLAG = False       # print message if all tries are exausted

# Generate and store the random number
randomNumber = random.randint(MIN_VALUE, MAX_VALUE)

# Print the number just for debugging
print("DEBUG PRINT: NUMBER IS = ", randomNumber)

# Begin for Loop for 3 iterations and compare the user input
for i in range(TRIES):
    userGuess = int(input("Enter your Guess = "))
    if userGuess == randomNumber:
        print("You guessed Correctly!")
        FLAG = True
        break
    else:
        print("Wrong Guess! Try Again")

# This approach was OK but why use an extra variable, when same could be achieved with existing variables?
# # Print win lose message
# if(FLAG):
#     print("\nYou WIN!\n")
# else:
#     print("\nBetter luck next time!\n")

# Print win lose message
if(userGuess == randomNumber):
    print("\nYou WIN!\n")
else:
    print("\nBetter luck next time!\n")

# End the program
print("***GoodBye!***")
