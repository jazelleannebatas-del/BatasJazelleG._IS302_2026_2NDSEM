class Animal_jab:
    def __init__(self_jab, name_jab):
        self_jab.name_jab = name_jab

    def speak(self_jab):
        print(self_jab.name_jab, "makes a sound")

class Dog_jab(Animal_jab):
    def bark(self_jab):
        print(self_jab.name_jab, "barks")

dog1_jab = Dog_jab("Buddy")
dog1_jab.speak()
dog1_jab.bark()