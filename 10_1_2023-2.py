from functools import reduce
def sum(accumulator, result):
    return accumulator + result

res = reduce(sum, range(1, 11))
print(res)
