def abbreviated(name):
    nameList = name.split(" ")
    shortName = ''
    for i in nameList:
        shortName += i[0]
    return shortName

name = input("Enter name ")
res = abbreviated(name)
print(res)
