def isExists(string, char):
    for i in range(len(string)):
        if string[i] == char: return i

string = input("Enter string ")
char = input("Enter char ")
res = isExists(string, char)
print(res)
