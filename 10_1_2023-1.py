def getAscii(list):
    return ord(list)

charList = ['p', 'y', 't', 'h', 'o', 'n']
res = map(getAscii, charList)
print(list(res))
