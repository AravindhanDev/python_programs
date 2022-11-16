def isEven(number):
    if number % 2 == 0: return True
    return False

number = int(input("Enter number: "))
res = isEven(number)
if res:
    print("It is even")
else:
    print("It is odd")
