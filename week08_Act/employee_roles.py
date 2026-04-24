class Employee_jab:
    def work_jab(self_jab):
        print("Employee performs tasks")

class Programmer_jab(Employee_jab):
    def work_jab(self_jab):
        print("Programmer writes code")

class Designer_jab(Employee_jab):
    def work_jab(self_jab):
        print("Designer creates UI designs")

employees_jab = [Programmer_jab(), Designer_jab()]
for emp_jab in employees_jab:
    emp_jab.work_jab()