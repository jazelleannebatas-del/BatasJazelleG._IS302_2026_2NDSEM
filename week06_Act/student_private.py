class Student_jab:
    def __init__(self_jab, name_jab, student_id_jab, gpa_jab):
        self_jab.__name = name_jab
        self_jab.__student_id = student_id_jab
        self_jab.__gpa = gpa_jab

    def get_student_info_nbs(self_jab):
        print("Name:", self_jab.__name)
        print("Student ID:", self_jab.__student_id)
        print("GPA:", self_jab.__gpa)

student1_jab = Student_jab("Juan", "2023-001", 1.75)
student1_jab.get_student_info_jab()