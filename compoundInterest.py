def compoundInterest(p, n, r):
    amount = p * (pow((1 + r / 100), n))
    ci = amount - p
    return ci

principle = float(input("Enter principle amount: "))
timeDuration = int(input("Enter time duration: "))
rateOfInterest = float(input("Enter rate of interest: "))
ci = compoundInterest(principle, timeDuration, rateOfInterest)
print(ci)
