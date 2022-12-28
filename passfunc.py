cubeOfNumber = lambda n : n ** 3
def cubeSum(cubeOfNumber, value):
    return cubeOfNumber(value)

value = int(input("Enter number "))
res = cubeSum(cubeOfNumber, value)
print(res)
