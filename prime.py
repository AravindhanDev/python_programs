def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1

primeStatus = isPrime(7)
print(primeStatus)
