class Employee_jab:
    def __init__(self_jab, name_jab):
        self_jab.__name = name_jab
        self_jab.__salary = 0

    def set_salary_jab(self_jab, salary_jab):
        if salary_jab > 0:
            self_jab.__salary = salary_jab

    def get_salary_jab(self_jab):
        return self_jab.__salary

emp_jab = Employee_jab("Ana")
emp_jab.set_salary_jab(30000)
print("Salary:", emp_jab.get_salary_jab())  