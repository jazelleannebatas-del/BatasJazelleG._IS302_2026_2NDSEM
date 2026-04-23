class Employee_jab:
    def __init__(self_jab, name_jab, salary_jab):
        self_jab.name_jab= name_jab
        self_jab.salary_jab = salary_jab

class Manager_jab(Employee_jab):
    def __init__(self_jab, name_jab, salary_jab, department_jab):
        super().__init__(name_jab, salary_jab)
        self_jab.department_jab= department_jab

    def display_manager_jab(self_jab):
        print("Name:", self_jab.name_jab)
        print("Salary:", self_jab.salary_jab)
        print("Department:", self_jab.department_jab)

manager1_jab = Manager_jab("John", 50000, "IT")
manager1_jab.display_manager_jab()