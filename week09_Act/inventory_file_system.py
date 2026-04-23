product_jab = input("Enter product name: ")
price_jab = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_jab + "," + price_jab + "\n")

print("Product saved successfully")