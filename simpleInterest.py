def simpleInterest(p,n,r):
    return (p * n * r) / 100

principle = float(input("Enter principle amount: "))
timeDuration = int(input("Enter time duration: "))
rateOfInterest = int(input("Enter rate of interest: "))
si = simpleInterest(principle, timeDuration, rateOfInterest)
print(si)
