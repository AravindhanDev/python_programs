def removeOddIndex(string):
    newStr = ''
    for i in range(len(string)):
        if i % 2 == 0:
            newStr += string[i]
    return newStr

string = input("Enter string ")
res = removeOddIndex(string)
print(res)
