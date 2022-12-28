def printWidth(value, width):
    string = '{:*<nd}'
    string = string.replace('n', str(width))
    print(string.format(value))

printWidth(17, 5)
