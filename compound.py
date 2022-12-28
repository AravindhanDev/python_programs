def compoundInterest(p, n, r):
    return p + (1 * (r / n)) ** n

p = float(input("Enter principle amount "))
n = float(input("Enter number of years "))
r = float(input("Enter rate of interest "))
ci = compoundInterest(p, n, r)

print(f"Compound interest {ci}")
