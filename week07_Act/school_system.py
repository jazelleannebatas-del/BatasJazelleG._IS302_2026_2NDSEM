class Person_jab:
    def __init__(self_jab, name_jab, age_jab):
        self_jab.name_jab= name_jab
        self_jab.age_jab= age_jab

    def display_info_jab(self_jab):
        print("Name:", self_jab.name_jab)
        print("Age:", self_jab.age_jab)

class Student_jab(Person_jab):
    def __init__(self_jab, name_jab, age_jab, course_jab):
        super().__init__(name_jab, age_jab)
        self_jab.course_jab = course_jab

    def display_info_jab(self_jab):
        super().display_info_jab()
        print("Course:", self_jab.course_jab)

class Teacher_jab(Person_jab):
    def __init__(self_jab, name_jab, age_jab, subject_jab):
        super().__init__(name_jab, age_jab)
        self_jab.subject_jab = subject_jab

    def display_info_jab(self_jab):
        super().display_info_jab()
        print("Subject:", self_jab.subject_jab)

# Example usage
student_jab = Student_jab("Maria", 20, "BSIS")
teacher_jab = Teacher_jab("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_jab.display_info_jab()
print("\nTeacher Info:")
teacher_jab.display_info_jab()