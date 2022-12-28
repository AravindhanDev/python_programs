def countString(string):
    countDict = {
        "digits": 0,
        "uppercase": 0,
        "lowercase": 0,
        "characters": 0,
        "specialCharacters": 0
    }
    for i in string:
        if i.isdigit():
            countDict['digits'] += 1
        if i.isalpha() and i == i.upper():
            countDict['uppercase'] += 1
        if i.isalpha() and i == i.lower():
            countDict['lowercase'] += 1
        if i.isalpha():
            countDict['characters'] += 1
        if i.isalnum() == False:
            countDict['specialCharacters'] += 1
    return countDict

string = input("Enter string ")
res = countString(string)
print(res)
    
