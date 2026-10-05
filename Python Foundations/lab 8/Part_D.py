class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"{self.name} is an Employee"


class Developer(Employee):
    def write_code(self):
        return f"{self.name} writes code"

class Manager(Employee):
    def hold_meeting(self):
        return f"{self.name} holds meetings"


employee_1 = Employee("Bob")
developer_1 = Developer("Harry")
manager_1 = Manager("John")

for employee in [employee_1, developer_1, manager_1]:
    print(employee.get_information())

print(developer_1.write_code())
print(manager_1.hold_meeting())

try:
    employee_1.write_code()
except AttributeError as e:
    print(f"Error : {e}")

# Python looks for write_code in Employee, but it only exists in Developer.
# A parent class cannot use methods that only exist in its child classes.

# note on __init__ plus super().__init__(...)
# New attributes mean __init__ plus super().__init__(...), and don't skip super()
# As soon as the child has its own __init__, Python finds it first and stops searching.
# The parent's __init__ no longer runs automatically, and super().__init__(name) is how you run it yourself.
