# Assignment 2
# This program takes User Name and Subject Marks and prints a Marks Sheet

# Gather Input from User
name = input("Enter your Name: ")
marksPhysics = int(input("Enter Marks in Physics (out of 100): "))
marksChemistry = int(input("Enter Marks in Chemistry (out of 100): "))
marksMath = int(input("Enter Marks in Math (out of 100): "))
marksComputers = int(input("Enter Marks in Computers (out of 100): "))
marksUrdu = int(input("Enter Marks in Urdu (out of 100): "))
marksEnglish = int(input("Enter Marks in English (out of 100): "))

# OPTIONAL, Clamp values below 100
marksPhysics = min(marksPhysics, 100)
marksChemistry = min(marksChemistry, 100)
marksMath = min(marksMath, 100)
marksComputers = min(marksComputers, 100)
marksUrdu = min(marksUrdu, 100)
marksEnglish = min(marksEnglish, 100)

# Calculate Total Marks Obtained by the user
marksObtained = marksPhysics + marksChemistry + \
    marksMath + marksComputers + marksUrdu + marksEnglish

totalMarks = 600    # Using a hard coded value of 600, this is generally not a good idea
# Calculate the Percentage Marks
percentMarks = (marksObtained / totalMarks) * 100

# Calculate Grade
grade = "F"

# The elif keyowrd is short for Else If in Plain English
if percentMarks > 80:
    grade = "A"
elif (percentMarks<80 and percentMarks>70):
    grade ="B"
elif(percentMarks<70 and percentMarks>50):
    grade = "C"
elif(percentMarks<50 and percentMarks>30):
    grade ="D"
else:
    grade = "F"     #this "else" is unecessary since grade is already default at F

# Print the mark sheet
# The \t is called a tab separator
# The \n is used for new line
# Either , or + can be used for strings but since we are taking input as numbers so + will not work
print("**********************************************\n\n")
print(">>>>>>>\t\t MARKS SHEET \t\t<<<<<<<")
print("|\tStudent Name: \t", name)
print("|\tPhysics: \t\t", marksPhysics, "/ 100")
print("|\tChemistry: \t\t", marksChemistry, "/ 100")
print("|\tMath: \t\t\t", marksMath, "/ 100")
print("|\tComputers: \t\t", marksComputers, "/ 100")
print("|\tUrdu: \t\t\t", marksUrdu, "/ 100")
print("|\tEnglish: \t\t", marksEnglish, "/ 100")
print("|")
print("|\tMarks Obtained: \t", marksObtained, "/", totalMarks)
print("|\tPercentage: \t\t", round(percentMarks, 2))
print("|\tGrade: \t\t\t", grade)
print(">>>>>>> _________________________________ <<<<<<<")

# End the program
print("*** GOODBYE! ***")
