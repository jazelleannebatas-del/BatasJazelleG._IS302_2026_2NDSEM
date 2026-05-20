PRODUCT_FILE_JAB = "products.txt"


def add_product_jab(product_jab):
    try:
        with open(PRODUCT_FILE_JAB, "a") as file_jab:
            file_jab.write(product_jab.get_product_info() + "\n")
    except Exception as error_jab:
        print("Error saving product:", error_jab)


def view_products_jab():
    try:
        with open(PRODUCT_FILE_JAB, "r") as file_jab:
            lines_jab = [
                line_jab.strip()
                for line_jab in file_jab
                if line_jab.strip()
            ]

        if not lines_jab:
            print("No products found.")
            return

        for line_jab in lines_jab:
            print(line_jab)

    except FileNotFoundError:
        print("No products found.")


def search_product_jab(product_id_jab):
    try:
        with open(PRODUCT_FILE_JAB, "r") as file_jab:
            for line_jab in file_jab:
                data_jab = [
                    field_jab.strip()
                    for field_jab in line_jab.strip().split(",")
                ]

                if len(data_jab) != 4:
                    continue

                if data_jab[0] == product_id_jab:
                    return data_jab

    except FileNotFoundError:
        pass

    return None


def update_product_quantity_jab(product_id_jab, new_quantity_jab):
    try:
        updated_jab = False
        lines_jab = []

        with open(PRODUCT_FILE_JAB, "r") as file_jab:
            for line_jab in file_jab:
                if not line_jab.strip():
                    continue

                data_jab = [
                    field_jab.strip()
                    for field_jab in line_jab.strip().split(",")
                ]

                if len(data_jab) != 4:
                    lines_jab.append(line_jab)
                    continue

                if data_jab[0] == product_id_jab:
                    data_jab[3] =
