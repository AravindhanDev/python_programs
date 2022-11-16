PI = 3.14

def areaOfCircle(radius):
    return PI * (radius ** 2)

radius = float(input("Enter radius: "))
area = areaOfCircle(radius)
print(area)
