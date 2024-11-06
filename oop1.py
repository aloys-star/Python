
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is studying")

accountant = Person("John", 25, "Male")
print(accountant.name)
print(accountant.age)
print(accountant.gender)
print(accountant.details())

Consultant = Person("Martha", 26, "Female")
print(Consultant.name)
print(Consultant.gender)
print(Consultant.age)
print(Consultant.details())

Doctor = Person("James", 32, "male")
print(Doctor.name)
print(Doctor.gender)
print(Doctor.age)
print(Doctor.details())