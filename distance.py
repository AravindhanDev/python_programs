import math

x1 = int(input("Enter first point coordinate x1 : "))
y1 = int(input("Enter first point coordinate y1 : "))
x2 = int(input("Enter first point coordinate x2 : "))
y2 = int(input("Enter first point coordinate y2 : "))

x = (x2 - x1) ** 2
y = (y2 - y1) ** 2
print(x, y)
distance = math.sqrt(x + y)
print("The Distance between two points: ", distance)
