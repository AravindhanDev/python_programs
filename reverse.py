def reverseNumber(r, number):
    if number == 0:
        return r
    else:
        r = (r * 10) + (number % 10)
        res = reverseNumber(r, number // 10)
    return res

n = int(input("Enter number "))
result = reverseNumber(0, n)
print(f"Reverse number is {result}")
    
