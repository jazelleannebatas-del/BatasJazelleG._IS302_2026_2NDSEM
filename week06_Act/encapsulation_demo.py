class Person_jab:
    def __init__(self_jab, name_jab, age_jab):
        self_jab.__name = name_jab
        self_jab.__age = age_jab

    def get_name_jab(self_jab):
        return self_jab.__name

    def get_age_jab(self_jab):
        return self_jab.__age

p1_jab= Person_jab("Maria", 20)
print("Name:", p1_jab.get_name_jab())
print("Age:", p1_jab.get_age_jab())