def insertKey(mydict, newkey, value):
    mydict[newkey] = value

def removeDuplicate(mydict):
    newDict = {}
    for key in mydict:
        if key not in newDict:
            newDict[key] = mydict[key]
    return newDict

res = removeDuplicate(mydict)
print(res)
