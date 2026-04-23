class Person_jab:
    def __init__(self_jab, name_jab, age_jab):
        self_jab.name_jab = name_jab
        self_jab.age_jab = age_jab

class Student_jab(Person_jab):
    def __init__(self_jab, name_jab, age_jab, course_jab):
        super().__init__(name_jab, age_jab)
        self_jab.course_jab = course_jab

    def display_student_jab(self_jab):
        print("Name:", self_jab.name_jab)
        print("Age:", self_jab.age_jab)
        print("Course:", self_jab.course_jab)

student1_jab = Student_jab("Maria", 20, "BSIS")
student1_jab.display_student_jab()