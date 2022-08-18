# Assignment 1
# Write program in which student can register in different courses:
# 1- Ask student name, age, email, phone no etc
# 2- Ask to choose from courses like ai, cnc, bcc,iot, web3 etc
# 3- Allow  student to select multiple courses
# 4- Save courses as list in student dictionary

# Variable for setting length of print string decorations
DECO = 7

# Declare a default student Dictionary to be used as template
studentDict = {"Name": "DefaultName",
               "Age": "0",
               "Email": "default@email.com"
               }

# List to store Student Records
studentRecords = list()

# List of Default Courses available
courseList = ["Artificial Intelligence", "Blockchain", "Cloud Native", "Internet of Things"]

# Function to print Main Menu (display options and get user input)

def mainMenu():
    print("\n\n")
    print("-" * DECO, "Main Menu", "-" * DECO)
    print("1. Add New Data")
    print("2. Display Existing Data")
    print("3. Quit Program\n\n")
    return int(input("Enter Choice: "))

# Function to add courses to student Data (called in addNewData() after user inputs basic details)

def addCourse(userDict):
    # Initialize an empty list for key "Courses"
    userDict["Courses"] = []
    print("-"*DECO, "Course Selection", "-"*DECO)
    # Iterate through Course List and ask user if they want to enroll or not
    for course in courseList:
        response = input(f"Do you want to enroll in {course}? (y/n): ")
        if(response.lower() == ("y" or "yes")):
            # Append course to Student Record key "Course"
            userDict["Courses"].append(course)
            print(f"[*] Enrolled in {course}")
        else:
            print(f"[*] Not Selected {course}")
    return userDict

# Function to add new student data

def addNewData():
    # Modify the global variable to maintain records between functions
    global studentRecords
    # Initialize a local copy of dictionary to store Student Data. This will be pushed to studentRecords List
    localDict = dict()
    print("\n\n")
    print("-" * DECO, "Add New Data", "-" * DECO)
    # Iterate through keys, values and get user input
    for key, value in studentDict.items():
        localDict[key] = input(f"Enter Student {key}: ")
    # Call function addCourse() to add Courses for this student
    localDict = addCourse(localDict)
    # Append to main record list
    studentRecords.append(localDict)

# Function to display Existing Data

def displayData():
    print("\n\n")
    print("-" * 7, "Display Exisiting Data", "-" * 7)
    # Get individual dictionary
    for rec in studentRecords:
        print("*" * DECO)
        # Print in form of Key, Value pair
        for key, value in rec.items():
            print(f"{key} = {value}")

# Main function to call all other functions

def main():
    userSel = 0
    # Start a While Loop and continue until user selects Quit Option
    while(userSel != 3):
        userSel = mainMenu()
        if(userSel == 1):
            addNewData()
        elif(userSel == 2):
            displayData()
        elif(userSel == 3):
            print("\n\nQuitting!\n\n")
        else:
            print("\n[ERROR] Invalid Option\n")


# Start Program
main()
print("***GOODBYE!***")
