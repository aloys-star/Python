
#A class is a blueprint of an object
#An Object is an instance of a class
class Person:

    # Property/Attribute/Variable/Characteristic
    name = "Patrick"
    age = 17
    height = 2.0

    #Method/Function/Behavior
    def walk(self):
        print("Person is walking")

#creating an object
accountant = Person()
accountant.walk()

teacher = Person()
teacher.walk()
