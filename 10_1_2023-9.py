vowels = ['a', 'e', 'i', 'o', 'u']
newList = [chr(char) for char in range(97, 123) if chr(char) not in vowels]
print(newList)
