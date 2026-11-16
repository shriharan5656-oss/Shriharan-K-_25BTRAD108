print("----- BILL GENERATOR -----")

item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n----- BILL -----")
print("Item     :", item)
print("Price    :", price)
print("Quantity :", quantity)
print("Total    :", total)
