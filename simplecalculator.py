num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operator = input("Choose an operator: ")

if operator == "1":
    print(num1 + num2)
elif operator == "2":
    print(num1 - num2)
elif operator == "3":
    print(num1 * num2)
elif operator == "4" and num2 == 0:
    print("Cannot be divided by zero")
elif operator == "4":
    print(num1 / num2)
else:
    print("Invalid operator")