# While loop
# increment
number = 20
while number <= 25:
    print(number)
    number += 1

num = 105
while num <= 110:
    print(num)
    num += 1

# Decrement
num = 10
while num >= 1:
    print(num)
    num -= 1

# Break and continue statement
# break
x = 25
while x <= 30:
    print(x)
    if x == 27:
        break
    x += 1

b = 0
while b < 5:
    b += 1
    if b == 3:
        continue
    print(b)

# For loop
for y in range(7):
    print(y)

for z in range(40, 45):
    print(z)

for mynumber in range(100, 121, 3):
    print(mynumber)

languages = ["Python", "Java", "C++", "Javascript"]
for lang in languages:
    print(lang)