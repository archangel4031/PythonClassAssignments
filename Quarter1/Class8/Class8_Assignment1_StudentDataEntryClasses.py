# Assignment 1
# Write program in which student can register in different courses:
# 1- Ask student name, age, email, phone no etc
# 2- Ask to choose from courses like ai, cnc, bcc,iot, web3 etc
# 3- Allow  student to select multiple courses
# 4- Save courses as list in student class

# Variable for setting length of print string decorations
DECO = 10

# Declare a class to hold Student Data

class StudentData():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.courses = []
    
    # Getter function for student courses
    def getStudentCourses(self):
        for course in self.courses:
            print(f"[->]Enrolled in {course}")
    
    # Setter function for student courses
    def setStudentCourses(self, newCourse):
        self.courses.append(newCourse)


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

def addCourse(studentObject):
    print("-"*DECO, "Course Selection", "-"*DECO)
    # Iterate through Course List and ask user if they want to enroll or not
    for course in courseList:
        response = input(f"Do you want to enroll in {course}? (y/n): ")
        if(response.lower() == ("y" or "yes")):
            # Append course to Student Record key "Course"
            studentObject.setStudentCourses(course)
            print(f"[*] Enrolled in {course}")
        else:
            print(f"[*] Not Selected {course}")
    return studentObject

# Function to add new student data

def addNewData():
    # Modify the global variable to maintain records between functions
    global studentRecords
    print("\n\n")
    print("-" * DECO, "Add New Data", "-" * DECO)

    # Get Input from user and create an object of type StudentData
    studentName = input("Enter Student Name: ")
    studentAge = input("Enter Student Age: ")
    studentEmail = input("Enter Student Email: ")

    # Create an object of StudentData and initialize with user inputs
    studentObject = StudentData(studentName, studentAge, studentEmail)

    # Pass to addCourse() function to enroll in courses
    studentObject = addCourse(studentObject)

    # Append the final object to list
    studentRecords.append(studentObject)

# Function to display Existing Data

def displayData():
    print("\n\n")
    print("-" * DECO, "Display Exisiting Data", "-" * DECO)
    # Get individual objects from list
    for rec in studentRecords:
        print("*" * DECO * DECO)
        print("Student Name: ", rec.name)
        print("Student Age: ", rec.age)
        print("Student Email: ", rec.email)
        print("Courses Enrolled in: ")
        rec.getStudentCourses()

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
