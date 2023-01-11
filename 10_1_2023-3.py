def even(number):
    return number % 2 == 0

numList = [12, 23, 34, 45, 56]
res = filter(even, numList)
print(list(res))
