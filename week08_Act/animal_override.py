class Animal_jab:
    def speak_jab(self_jab):
        print("Animal makes a sound")

class Dog_jab(Animal_jab):
    def speak_jab(self_jab):
        print("Dog barks")

class Cat_jab(Animal_jab):
    def speak_jab(self_jab):
        print("Cat meows")

animals_jab = [Dog_jab(), Cat_jab()]
for animal_jab in animals_jab:
    animal_jab.speak_jab()