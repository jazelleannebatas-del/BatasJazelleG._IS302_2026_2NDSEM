class Car_jab:
    def __init__(self_jab, brand_jab, model_jab, year_jab):
        self_jab.brand_jab = brand_jab
        self_jab.model_jab = model_jab
        self_jab.year_jab = year_jab
    
    def display_car_jab(self_jab):
        print(self_jab.brand_jab, self_jab.model_jab, self_jab.year_jab)

car1_jab = Car_jab("Toyota", "Corolla", 2020)
car1_jab.display_car_jab()
