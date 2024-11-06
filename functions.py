# Inbuilt Functions
y = max(230, 345, 92, 349, 2345)
print("The maximum value is", y)

x = min(230, 345, 92, 349, 2345)
print("The minimum value is", x)

z = pow(2,3)
print("2 to the power of 3 is", z)

# User-defined function
def student():
    print("Aloys")

student() #Calling the function

def person():
    print("person is walking")
person()


#parameters and arguments
def add(num1,num2):
    print(num1 + num2)

add(23,32)
add(23, 45)

def employee(full_name,age,email,position,marital_status):
    print(full_name,age,email,position,marital_status)

employee("John",23,"john234@gmail.com","HR","single")
employee("Rose",22,"roesn234@gmail.com","MD","single")
employee("Owen",23,"oewmn234@gmail.com","CEO","single")
employee("Jane",25,"janeww34@gmail.com","CFO","single")
employee("James",21,"jamse34@gmail.com","CMO","single")


