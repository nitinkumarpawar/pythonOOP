class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def fullname(self):
        return self.name


emp_1 = Employee("John", 10000)
emp_2 = Employee("Jane", 20000)

print(emp_1.fullname())
print(emp_1.salary)
print(emp_2.fullname())
