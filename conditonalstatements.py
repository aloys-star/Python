teperature = 32

if teperature < 25:
    print("it is cold")
elif teperature > 25:
    print("it is hot")
else:
    print("normal temperature")

#A program that returns the largest number among three numbers
first = 56
second = 23
third = 78

if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")

#A program that checks whether a number is even or odd
num = 6

if num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#A program that returns the area of a rectangle
# A = l * w
length = 20
width = 10
area = length * width
print("The area is ", area)

#A program that returns the area of a trapezium
#A = 0.5 * (a + b) * h
a = 20
b = 30
height = 5
area = 0.5 * (a + b) * height
print("The area is ", area)