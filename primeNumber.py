def checkPrimes(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            return False

    return isPrime

def primeRanges(number):
    for i in range(2, number):
        if checkPrimes(i):
            print(i, " is prime number")


primeRanges(100)

