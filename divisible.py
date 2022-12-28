def divisible(m, n):
    resArr = []
    if m > n: return resArr
    for i in range(1, n):
        if i % m == 0:
            resArr.append(i)
    return resArr

resultArr = divisible(5, 100)
print(resultArr)
