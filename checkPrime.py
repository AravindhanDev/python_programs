def checkPrimes(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            return "Not a Prime number"

    return "Prime number"

res = checkPrimes(97)
print(res)
