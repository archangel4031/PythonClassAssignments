# File path

fpath = "../Extras/commands.txt"
fileCounter = 0

fileObject = open(fpath, "r")

for line in fileObject.readlines():
    print(line)

    # Create a file name based on counter
    subFileName = "./SubFile" + str(fileCounter) +".txt"

    # Check if CRLF encounterd, if not appped to existing file
    if(line !="\n"):
        with open(subFileName, "a+") as file:
            file.write(line)
    # if CRLF present, increment counter to create a new file
    else:
        fileCounter += 1

# End the program
print("***GOODBYE***")
    