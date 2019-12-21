class Employee:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def fullname(self):
        return self.name + " " + self.lastname

    def salary(self):
        self.salary = 5000
        return self.salary


class Manager(Employee):
    def __init__(self, name, lastname, age, access_control):
        self.access_control = access_control
        # self.salary = salary
        super().__init__(name, lastname, age)

    def salary(self):
        self.salary = 500000
        return self.salary


class Intern(Employee):
    def __init__(self, name, lastname, age, stipend, duration):
        self.stipend = stipend
        self.duration = duration
        super().__init__(name, lastname, age)

    def overall_income(self):
        return self.stipend * self.duration


m1 = Manager("Sam", "Worth", 49, True)

print(m1.fullname())
print(m1.salary())

i1 = Intern("Dean", "Billings", 22, 500, 3)
print(i1.overall_income())
