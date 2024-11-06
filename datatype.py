#Datatype

number = 60  # int
num = 23.93  # float
greeting = "hello there"  # str
isPythonIntresting = True  # boolean

fruits = ["apple", "banana", "cherry"]  # list

cars = ("bmw", "toyota", "audi") # tuple

countries = {"kenya", "tanzania", "Ethiopia"} # set

student = {
    "firstname" : "Aloys",
    "age" : 20,
    "course" : "MIT",
    "nationality" : "Kenya",
} #Dictionary

print(num)
print(isPythonIntresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])

#determining the datatype

print(type(isPythonIntresting))
print(type(cars))

#typecasting- Converting one datatype to another

print(int(num))
print(float(60))