def capitalizeFirstChar(string):
    return string[0].upper() + string[1:].lower()

def capitalize(string):
    strList = string.split(" ")
    newList = []
    for i in strList:
        newList.append(i[0].upper() + i[1:].lower())
    return ' '.join(newList)

def alternateCase(string):
    newStr = ''
    for i in string:
        if i == i.upper():
            newStr += i.lower()
        else:
            newStr += i.upper()
    return newStr

string = input("Enter string ")
res = alternateCase(string)
print(res)



