class Student:
    def __init__(self, student_id_jab, name_jab, course_jab):
        self.student_id_jab = student_id_jab
        self.name_jab = name_jab
        self.course_jab = course_jab

    def display_info(self):
        print(self.student_id_jab, self.name_jab, self.course_jab)

    def to_record(self):
        return f"{self.student_id_jab},{self.name_jab},{self.course_jab}\n"
