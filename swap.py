num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

print("Before -> number1: {}, number2: {}".format(num1, num2))

temp = num1
num1 = num2
num2 = temp

print("After -> number1: {}, number2: {}".format(num1, num2))
