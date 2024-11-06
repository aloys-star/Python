#Arithmetic operators
num1 = 10
num2 = 3

print(num1 + num2) #addition
print(num1 - num2) #subtarction
print(num1 * num2) #multiplication
print(num1 / num2) #division
print(num1 % num2) #modulus- returns remainder

#Comparison operators
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2)

#Assignment operators
x = 100
print(x)

x += 2
print(x)

y = 56
y -= 3
print(y)

#logic operators- and, or, not
a = 23
print(a < 40 and a > 2)
print(a < 40 or a > 2)
print(not (a < 40 or a > 2))

#operator precedence
result = (10+6/2-4)
print(int(result))