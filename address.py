address = input("Enter address: ")
result = address.replace(", ", ",\n")
lastIndex = result[-1]
if lastIndex != '.':
    result += '.'

print(result)
