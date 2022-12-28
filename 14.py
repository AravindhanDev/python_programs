def printWidth(value, width):
    string = '{:0>nd}'
    string = string.replace('n', str(width))
    print(string.format(value))

printWidth(17, 3)
