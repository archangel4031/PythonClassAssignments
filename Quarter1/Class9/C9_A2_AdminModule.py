# Import necessary modules
from C9_A2_BaseModule import ItemInfo, DECO, sleep

# Class used to define what an Admin can do
class Admin():
    def __init__(self, adminID):
        self.adminID = adminID
    
    # Method to add a new item to inventory. Ask for item details and append to working copy of Online Store List
    def addNewItem(self, inItemList):
        itemCode = len(inItemList) + 1
        itemName = input("Enter Item Name:\t")
        itemDesc = input("Enter Item Description:\t")
        itemPrice = input("Enter Item Price:\t")
        itemQty = input("Enter Item Quantity:\t")
        newItem = ItemInfo(itemCode, itemName, itemDesc, itemPrice, itemQty)
        inItemList.append(newItem)
        print("[i] New Item Added Successfully!")
        sleep(1)

    # Method to view sales records
    def viewTodaysSales(self, inCustomerRecords):
        print("-" * DECO, "SALES RECORDS", "-" * DECO)
        for customer in inCustomerRecords:
            print("==============================================================")
            print("Customer Name:\t", customer.customerID)
            print("Items bought are")
            for item in customer.shoppingCart:
                print("-->Item Code:\t", item.itemCode)
                print("-->Item Name:\t", item.itemName)
                print("-->Bought Quantity:\t", item.itemQty)
    
    # Method to increase quantity of existing items
    def increaseQtyExisting(self, inItemList):
        print()
        print("-" * DECO, "UPDATE EXISTING ITEM", "-" * DECO)
        print("\n\n")
        userSel = int(input("Enter Item Code: "))
        userQty = int(input("Enter Quantity: "))
        if(userSel > len(inItemList)):                 # Check index of item which is equal to item code minus 1
            print("[w] Item not found!")
        else:
            print("[i] Found Item:\t\t", inItemList[userSel-1].itemName)
            inItemList[userSel-1].itemQty+=userQty
            print(f"[i] Successfully added {userQty} quantity to {inItemList[userSel-1].itemName}")
# ----------------- END CLASS DEFINITION -----------------

# FN: Print Admin Menu and get selection
def printAdminMenu():
    print("1. Add New Item")
    print("2. View Today's Sales Record")
    print("3. Add stock to Existing Item")
    print("4. Back to Main Menu")
    return int(input("\n\nEnter Selection: "))

# FN: Handle input from Admin
def handleAdminSelection(inAdmin, inItemList, inCustomerRecords):
    inSel = 0
    while(inSel != 4):
        print("\n\n")
        print("-" * DECO, "Admin Menu", "-" * DECO)
        print("Welcome Admin! ", inAdmin.adminID)
        inSel = printAdminMenu()
        if(inSel == 1):
            inAdmin.addNewItem(inItemList)
        elif(inSel == 2):
            inAdmin.viewTodaysSales(inCustomerRecords)
        elif(inSel == 3):
            inAdmin.increaseQtyExisting(inItemList)
        elif(inSel == 4):
            break
        else:
            print("[w] Invalid Option")

# FN: Main function for Admin
def adminMain(inItemList, inCustomerRecords):
    adminID = input("Enter Admin Name: ")
    adminObject = Admin(adminID)
    handleAdminSelection(adminObject, inItemList, inCustomerRecords)