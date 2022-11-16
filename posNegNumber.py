def checkPositive(num):
    if num < 0: return False
    return True

num = int(input("Enter number: "))
res = checkPositive(num)

if res:
    print(num, "is Positive Integer")
else:
    print(num, "is Negative Integer")
    
