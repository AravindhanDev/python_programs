list = []

def generateInvoice(list):
    print("\n***************************BILL*************************")
    print("Item Names	        Item Quantity		 Item Price")
    print()
    total = 0
    for i in range(len(list)):
        print("{}	        {} Qty		         ₹{}".format(list[i][0], list[i][1], list[i][2]))
        total += list[i][1] * list[i][2]
    print("*******************************************************")
    print("Total Amount to be paid ₹{}".format(total))
    print("*******************************************************")

def getProducts(list):
    choice = 1
    while choice != -1:
        print()
        itemsPurchased = input("Item Name: ")
        purchasedQuantity = int(input("Item Quatity: "))
        pricePerUnit = int(input("Item Price: "))
        list.append([itemsPurchased, purchasedQuantity, pricePerUnit])
        choice = int(input("Add (-1 for exit)? "))

print("***************************SHOP*************************")
print()
getProducts(list)
generateInvoice(list)


