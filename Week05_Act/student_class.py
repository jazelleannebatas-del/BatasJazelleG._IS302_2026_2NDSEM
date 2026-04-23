class Student_jab:
    def __init__(self_jab, name_jab, student_id_jab, course_jab):
        self_jab.name_jab = name_jab
        self_jab.student_id_jab = student_id_jab
        self_jab.course_jab = course_jab
    
    def display_student_jab(self_jab):
        print("Name:", self_jab.name_jab)
        print("Student ID:", self_jab.student_id_jab)
        print("Course:", self_jab.course_jab)

student1_jab = Student_jab("Maria", "2023-001", "BSIS")
student1_jab.display_student_jab()
