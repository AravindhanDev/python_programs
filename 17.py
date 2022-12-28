def stripFromString(string, stripString):
    return string.strip(stripString)

string = input("Enter string ")
stripString = input("Enter strip string ")
res = stripFromString(string, stripString)
print(res)
