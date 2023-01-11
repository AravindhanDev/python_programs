def func1(alphaList):
    return alphaList[0:3]

def func2(alphaList):
    return alphaList[4:7]

def func3(alphaList, index):
    return alphaList[index:]

alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(func1(alphaList))
print(func2(alphaList))
print(func3(alphaList, 6))

