def encryption(string, key):
    newStr = ''
    for i in string:
        newStr += chr(ord(i) + 3)
    return newStr

res = encryption("aravindhan", 5)
print(res)
