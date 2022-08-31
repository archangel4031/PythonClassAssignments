# Assignment 2
# Make file about store inventory (product name, description, quantity in stock). Create csv file or text file, your preference.
# Write Program to ask whether you are admin or customer.
# For Admin
#     -    Can create new products 
#     -    Can see sales statistics such as sales amount & quantity
# For customer 
#     -    Can view products
#     -    See details of product
#     -    Option should be do you want to purchase item
#     -    If customer required item quantity is less than available items, allow customer to buy item and create update in inventory records.
#     -    If customer required item quantity is more than available items, tell user the minimum items that customer can buy

# 1)- Admin has authority to see sale record and add new products.
# 2)- Customer has access to product list/ choice menu,
# 3)update inventory record and also create sales record, showing items sold.

# Import all sub Modules
from C9_A2_BaseModule import *                  # In plain English, this is like "from module import everything"
from C9_A2_CustomerModule import *
from C9_A2_AdminModule import *

# Create an empty list to store CSV Content, this will be our working copy of Online Store
CSVContentList = []

# Create a List to store Each Item Object
ItemObjectDatabase = []

# Create a list of customers that checked in today, will be used to update sales records
CustomerDatabase = []

# Import CSV File and store a working copy in Memory
# Open CSV File. The "with" method to open and read files looks ugly :')
fileCSV = open(inFilePath, "r")
fileContent = csv.reader(fileCSV)

# Load content of file in the list declared earlier, one row per line
for line in fileContent:
    CSVContentList.append(line)

# Fill ItemObjectDatabase List with information from CSV
for row in CSVContentList:
    storeItemObjectList(row, ItemObjectDatabase)

# FN: Build Main Menu and ask user selection
def mainMenu():
    system("cls")
    print("-" * DECO, "Main Menu", "-" * DECO)
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Quit")
    return int(input("\n\nEnter Selection: "))

# The Main Program Code
def main():
    userSel = 0
    while(userSel != 3):
        userSel = mainMenu()
        if(userSel == 1):
            system("cls")
            adminMain(ItemObjectDatabase, CustomerDatabase)
        elif(userSel == 2):
            system("cls")
            customerMain(ItemObjectDatabase, CustomerDatabase)
        elif(userSel == 3):
            print("[i] Quitting")
        else:
            print("[w] Invalid Option")


# ------------------- Begin Main Program ------------------- 
main()
print()
print("*** GOODBYE ***")