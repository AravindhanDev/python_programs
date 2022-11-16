str = ''
for i in range(1, 101):
    if i % 3 == 0: str += 'fizz'
    if i % 5 == 0: str += 'buzz'
    print(i if str == '' else str)
    str = ''
