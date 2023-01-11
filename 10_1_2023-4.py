'''
numbers = [1, 2, 3, 4]
newlist = [str(number) + 'a' for number in numbers]
print(newlist)
'''

'''
charList = [i + j for i in 'ab' for j in 'bcd']
print(charList)
newList = [charList[i] for i in range(6) if i % 2 == 0]
print(newList)
'''

newList = [i * 10 for i in range(1, 11)]
print(newList)
