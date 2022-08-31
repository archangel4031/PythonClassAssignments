import csv
from os import system

# Variable for setting length of print string decorations
DECO = 10

# Set file path for CSV File
inFilePath = "./Quarter1/Class9/CSVFiles/QuizFile.csv"
outFilePath = "./Quarter1/Class9/CSVFiles/QuizResults.csv"

# Declare a class for User Data
class UserInfo():
    def __init__(self, UserID="0", UserName="user0"):
        self.UserID = UserID
        self.UserName = UserName
        self.UserPercentage = 0

    # Setter for UserPercentage
    def SetUserPercentage(self, inPercent):
        self.UserPercentage = inPercent

    # Getter / Print for UserInfo based on ID
    def GetUserInfo(self):
        print("User ID: ", self.UserID)
        print("User Name: ", self.UserName)
        print("Obtained Percentage: ", self.UserPercentage)


# FN: Function for printing Questions from CSV file
def PrintQuestion(InListLine, DECO):
    print(InListLine[0], ": ", InListLine[1])
    print("=" * DECO)

# FN: Function for printing MCQ options and getting user input
def GetUserOption(InListLine):
    counter = 1
    for option in InListLine[2:-1]:
        print("Option ", counter, ": ", option)
        counter += 1
    return int(input("\n\nSelect one option: "))

# FN: Retrieve the correct answers from the CSV Line, the last index entry
def GetCorrectAnswers(InListLine, outCorerctAnswerList):
    for answer in InListLine[-1]:
        outCorerctAnswerList.append(int(answer))
    # Do not use return, list is mutable (remember this for God's sake man, this is not C++)

# FN: Calculate percentage by comparing correct answers with user responses
def CalculatePercentage(userAnswers, correctAnswers):
    score = 0
    for i in range(0, len(userAnswers)):
        if(userAnswers[i] == correctAnswers[i]):
            score += 1
    percentage = score / 5
    return percentage * 100

# FN: Get and Store User Data in Main List
def GetAndStoreUserID():
    UserID = input("Enter your User ID: ")
    UserName = input("Enter your User Name: ")
    UserObject = UserInfo(UserID, UserName)
    return UserObject

# FN: New User wants to attempt Quiz. DO NOT WISH THEM GOOD LUCK :P 😛
def NewUserQuiz(inUserDatabase, CSVContentList, CSVCorrectAnswers):
    userResponse = []
    currentUser = GetAndStoreUserID()
    for CSVLine in CSVContentList[1:]:
        system("cls")                   # Clear console before each Question
        PrintQuestion(CSVLine, DECO)
        userResponse.append(GetUserOption(CSVLine))
    percent = CalculatePercentage(userResponse, CSVCorrectAnswers)
    currentUser.SetUserPercentage(percent)
    inUserDatabase.append(currentUser)

# FN: Display stored User Info in Database List
def DisplayExistingUserScore(inUserDataBase):
    system("cls")
    for user in inUserDataBase:
        print("-" * DECO * DECO)
        user.GetUserInfo()


# FN: Save User Info Database List to a CSV file, in append mode
def SaveToCSVFile(filePath, inUserDatabase):
    fileObject = open(filePath, "a", newline="")
    fileHandler = csv.writer(fileObject, delimiter=",")
    for user in inUserDatabase:
        fileHandler.writerow([user.UserID, user.UserName, user.UserPercentage])
    fileObject.close()
    print("File Written Successfully!")

# FN: Print Main Menu and get user input option
def mainMenu(DECO):
    print("\n\n")
    print("-" * DECO, "Main Menu", "-" * DECO)
    print("1. Attempt Quiz")
    print("2. Display Existing User Scores")
    print("3. Save User Database to CSV File")
    print("4. Quit Program\n\n")
    return int(input("Enter Choice: "))
