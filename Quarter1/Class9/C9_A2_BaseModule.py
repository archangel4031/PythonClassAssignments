# import necesary modules
import csv
from os import system
from time import sleep

# Variable to make decorations
DECO = 10

# Set file path for CSV File
inFilePath = "./Quarter1/Class9/CSVFiles/OnlineStore.csv"
outFilePath = "./Quarter1/Class9/CSVFiles/OnlineStoreOutputRecords.csv"

# Class to define what attributes an item should have
class ItemInfo():
    def __init__(self, itemCode, itemName, itemDesc, itemPrice, itemQty):
        self.itemCode = itemCode
        self.itemName = itemName
        self.itemDesc = itemDesc
        self.itemPrice = int(itemPrice)
        self.itemQty = int(itemQty)
    
    # Get available quantity in store
    def IsQtySufficient(self, requestedQty):
        if(requestedQty > self.itemQty):
            return False
        else:
            return True
    
    # Decrease the Quantity in store
    def DecreaseQty(self, amount):
        self.itemQty-=amount


# FN: Get item row and make ItemInfo Objects and store in List
def storeItemObjectList(inItemRow, inItemDatabase):
    itemObject = ItemInfo(inItemRow[0], inItemRow[1], inItemRow[2], inItemRow[3], inItemRow[4])
    inItemDatabase.append(itemObject)
