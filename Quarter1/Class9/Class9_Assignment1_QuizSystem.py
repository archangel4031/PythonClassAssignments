# Assignment 1
# Write MCQ based questions with options and right answer in one file. Create csv file or text file, your preference.
# Ask ID from users to take quiz and store their answer, at the end calculate and print total percentage.

# Import the modules
from C9_A1_ModuleFile import *

# Create an empty list to store CSV Content
CSVContentList = []
# Create a list to store correct answers
CSVCorrectAnswers = []
# Declare empty dictionary variable to store User Class List
UserInfoDatabase = []

# Open CSV File. The "with" method to open and read files looks ugly :')
fileCSV = open(inFilePath, "r")
fileContent = csv.reader(fileCSV)

# Load content of file in the list declared earlier, 0 index is column label
for line in fileContent:
    CSVContentList.append(line)
# Store correct answers, in this case they are stored at last value in each row of CSV
for line in CSVContentList[1:]:
    GetCorrectAnswers(line, CSVCorrectAnswers)

# FN: The main function to be called
def main():
    userSel = 0
    # Start a While Loop and continue until user selects Quit Option
    while(userSel != 4):
        userSel = mainMenu(DECO)
        if(userSel == 1):
            NewUserQuiz(UserInfoDatabase, CSVContentList, CSVCorrectAnswers)
        elif(userSel == 2):
            DisplayExistingUserScore(UserInfoDatabase)
        elif(userSel == 3):
            SaveToCSVFile(outFilePath, UserInfoDatabase)
        elif(userSel == 4):
            print("\n\nQuitting!\n\n")
        else:
            print("\n[ERROR] Invalid Option\n")


# -------------------------- Begin Main Code --------------------------
system("cls")
main()
fileCSV.close()
print("***GOODBYE***")
