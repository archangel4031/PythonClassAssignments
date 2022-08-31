# Import necessary Modules
from C9_A2_BaseModule import DECO, sleep

# Class used to define what a Customer can do
class Customer():
    def __init__(self, customerID):
        self.customerID = customerID
        self.cashBalance = 50000        # Give an initial cash of 50,000 units
        self.shoppingCart = []
    
    # Method Decrease Cash Balance in case of successful purchase
    def DecreaseBalance(self, amountToDecrease):
        self.cashBalance-=amountToDecrease
    
    # Method to find out remaing cash Balance
    def GetRemainingBalance(self):
        print("\n\n")
        print("Remaining Balance: ", self.cashBalance)
    
    # Method to print all items available to Customer
    def ViewAllItems(self, inItemList):
        for item in inItemList:
            print("==============================================================")
            print("Item Code:\t", item.itemCode)
            print("Name:\t\t", item.itemName)
            print("Description:\t", item.itemDesc)
            print("Price:\t\t", item.itemPrice)
            print("Qty:\t\t", item.itemQty)
            print()
        sleep(1)

    # Method to buy item using Item Code
    def BuyItem(self, inItemList):
        print("-" * DECO, "BUY ITEM", "-" * DECO)
        print("\n\n")
        userSel = int(input("Enter Item Code: "))
        userQty = int(input("Enter Quantity: "))
        if(userSel > len(inItemList)):                 # Check index of item, which is equal to item code minus 1. If user input is greater than length then it is a wrong input
            print("[w] Item not found!")
        else:
            print("[i] Found Item:\t\t", inItemList[userSel-1].itemName)
            if(self.cashBalance >= inItemList[userSel-1].itemPrice * userQty):            # Check cash balance of customer
                if(inItemList[userSel-1].IsQtySufficient(userQty)):                       # Check if requested quantity is available in store
                    self.DecreaseBalance(inItemList[userSel-1].itemPrice * userQty)       # YES, decrease cash of customer
                    inItemList[userSel-1].DecreaseQty(userQty)                            # YES, decrease quantity from store
                    shoppingCartItemObject = inItemList[userSel-1]                        # Create a replica of Item Object to add to shopping cart
                    shoppingCartItemObject.itemQty = userQty                              # Change the quantity attribute to reflect quantity user bought instead of quantity held in inventory
                    self.shoppingCart.append(shoppingCartItemObject)                      # Add to shopping cart which will be used to update store sales records
                    print("[i] Bought:\t\t", shoppingCartItemObject.itemName)
                    print("[i] Bought Quantity:\t", shoppingCartItemObject.itemQty)
                else:
                    print("[w] Insufficient Quantity in Store")
            else:
                print("[w] Insufficient Cash Balance")             
        sleep(1)
# ----------------- END CLASS DEFINITION -----------------


# FN: Print Customer Menu and get selection
def printCustomerMenu():
    print("1. View Store Items")
    print("2. Check Balance")
    print("3. Buy Item")
    print("4. Back to Main Menu")
    return int(input("\n\nEnter Selection: "))

# FN: Handle input from Customer
def handleCustomerSelection(inCustomer, inItemList):
    inSel = 0
    while(inSel != 4):
        print("\n\n")
        print("-" * DECO, "Customer Menu", "-" * DECO)
        print("Welcome Customer! ", inCustomer.customerID)
        inSel = printCustomerMenu()
        if(inSel == 1):
            inCustomer.ViewAllItems(inItemList)
        elif(inSel == 2):
            inCustomer.GetRemainingBalance()
        elif(inSel == 3):
            inCustomer.BuyItem(inItemList)
        elif(inSel == 4):
            break
        else:
            print("[w] Invalid Option")

# FN: Main function for Customer
def customerMain(inItemList, inCustomerList):
    customerID = input("Enter Customer Name: ")
    customerObject = Customer(customerID)
    handleCustomerSelection(customerObject, inItemList)
    inCustomerList.append(customerObject)