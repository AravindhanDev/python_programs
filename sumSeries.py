# series 1
'''number = int(input("Enter range: "))
sum = (number * (number + 1)) / 2
print("Sum of the series is: ", sum)'''

#series 2
'''x = int(input("Enter x: "))
n = int(input("Enter range: "))
sum = 0
negative = True
for i in range(1, n+1):
    if negative:
        sum = sum + (-(x ** i))
        negative = False
    else:
        sum = sum + (x ** i)
        negative = True

print("Sum of series is: ", sum)'''

#series 3
'''number = int(input("Enter number: "))
sum = 0
for i in range(1, number+1):
    for j in range(1, i+1):
        sum += j

print(sum)'''

#series 4
'''from fractions import Fraction

def fact(num):
    if num == 1: return 1
    return num * fact(num-1)

x = int(input("Enter x: "))
num = int(input("Enter number: "))
sum = 0

for i in range(1, num+1):
    sum += ((x ** i) / fact(i)) 

sum = str(Fraction(1 - sum).limit_denominator())
    
print("Sum of series: ", str(Fraction(sum).limit_denominator()))'''
