# Made for difference of Mutable and Immutable data types

# Variable of different types
mutableList = [1, 2, 3, 4]
immutableInteger = 99


def appendInteger(inList, inInteger):
    print("[i] Inside function")
    
    # Print Memory Values before change
    print("Mem value of inList:\t\t", hex(id(inList))[-4:])
    print("Mem value of inInteger:\t\t", hex(id(inInteger))[-4:])
    print("Mem value of mutableList:\t", hex(id(mutableList))[-4:])
    # print("Mem value of immutableInteger:\t\t", hex(id(immutableInteger)))            # ERROR on this line

    # Change local variable values
    inInteger += 1
    inList.append(inInteger)
    print("[i] Local Variables changed")

    # Change global variables
    mutableList.append(88)
    immutableInteger = 77
    print("[i] Global variables chaged")

    # Print Memory Values after change
    print("Mem value of inList:\t\t", hex(id(inList))[-4:])
    print("Mem value of inInteger:\t\t", hex(id(inInteger))[-4:])
    print("Mem value of mutableList:\t", hex(id(mutableList))[-4:])
    print("Mem value of immutableInteger:\t", hex(id(immutableInteger))[-4:])
    
    # End the function. Add a print statement to update Variables in Breakpoint View
    print("[i] Function routine completed")


print("[i] Start from main code")
# Print Memory values before calling function
print("Mem value of mutableList:\t", hex(id(mutableList))[-4:])
print("Mem value of immutableInteger:\t", hex(id(immutableInteger))[-4:])

# Call function
appendInteger(mutableList, immutableInteger)

# Print Memory values after calling function
print("Mem value of mutableList:\t", hex(id(mutableList))[-4:])
print("Mem value of immutableInteger:\t", hex(id(immutableInteger))[-4:])

print("***GOODBYE***")

