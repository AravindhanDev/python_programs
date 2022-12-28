def findOccurances(string, char):
    count = 0
    for i in string:
        if i == char: count+=1
    return count

string = input("Enter string ")
char = input("Enter char ")
res = findOccurances(string, char)
print(res)
