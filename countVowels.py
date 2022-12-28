def getVowelsCount(sentense):
    vowelsCount = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for i in sentense:
        if i == 'a': vowelsCount[i]+=1
        if i == 'e': vowelsCount[i]+=1
        if i == 'i': vowelsCount[i]+=1
        if i == 'o': vowelsCount[i]+=1
        if i == 'u': vowelsCount[i]+=1
    return vowelsCount

sentense = input("Enter sentense ")
vowelsCount = getVowelsCount(sentense)
print(vowelsCount)
            
