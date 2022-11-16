def amstrongNumber(num, sum):
    temp = num
    length = len(str(num))
    while temp > 0:
       digit = temp % 10
       sum += digit ** length
       temp //= 10

    if num == sum:
        return "It is an amstrong number"
    else:
        return "It is not an amstrong number"

num = int(input("Enter a number: "))
res = amstrongNumber(num, 0)
print(res)



