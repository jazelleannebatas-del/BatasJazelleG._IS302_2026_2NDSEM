class Product_jab:
    def __init__(self_jab, name_jab, price_jab, quantity_jab):
        self_jab.__name = name_jab
        self_jab.__price = price_jab
        self_jab.__quantity = quantity_jab

    def get_product_info_jab(self_jab):
        print("Product:", self_jab.__name)
        print("Price:", self_jab.__price)
        print("Quantity:", self_jab.__quantity)

    def update_quantity_jab(self_jab, new_quantity_jab):
        if new_quantity_jab>= 0:
            self_jab.__quantity = new_quantity_jab

    def update_price_nbs(self_jab, new_price_jab):
        if new_price_jab > 0:
            self_jab.__price = new_price_jab

# Example usage
product_jab = Product_jab("Laptop", 45000, 10)
product_jab.get_product_info_jab()