def cubeSum(num):
    return ((num * (num + 1))/2) ** 2 

num = int(input("Enter number: "))
res = cubeSum(num)
print(int(res))
