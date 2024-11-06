firstname = input("Enter your first name: ")
print("My first name is", firstname)

lastname = input("Enter your last name: ")
print("My last name is", lastname)

Age = int(input("Enter your Age: "))
print("I am ", Age, "years old")

#A program that returns the smallest number among 4 inputed numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 < num2 and num1 < num3:
    print("The first number is smallest")
elif num2 < num1 and num2 < num3:
    print("The second number is smallest")
else:
    print("The third number is smallest")