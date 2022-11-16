def factorial(num):
    if num == 1: return 1
    return num * factorial(num-1)

number = int(input("Enter number: "))
output = factorial(number)
print(output)
