class Product:
    def __init__(self, product_id_jab, name_jab, price_jab, quantity_jab):
        self.__product_id_jab = product_id_jab
        self.__name_jab = name_jab
        self.__price_jab = price_jab
        self.__quantity_jab = quantity_jab

    def get_product_info(self):
        return (
            f"{self.__product_id_jab},"
            f"{self.__name_jab},"
            f"{self.__price_jab},"
            f"{self.__quantity_jab}"
        )

    def get_id(self):
        return self.__product_id_jab

    def update_quantity(self, quantity_jab):
        self.__quantity_jab = quantity_jab

    def get_quantity(self):
        return self.__quantity_jab

    def __str__(self):
        return (
            f"{self.__product_id_jab} "
            f"{self.__name_jab} "
            f"{self.__price_jab} "
            f"{self.__quantity_jab}"
               )
