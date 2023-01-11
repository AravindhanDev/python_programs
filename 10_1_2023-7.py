def func(words, char):
    newWords = []
    for word in words:
        for i in range(len(word)):
            if char == word[i] and i == 0:
                newWords.append(word)
    return newWords

words = ['aravindhan', 'ashok', 'prakash', 'ajay', 'fameen', 'srisankar', 'manoj']
char = input("Enter alphabet ")
res = func(words, char.lower())
print(res)
