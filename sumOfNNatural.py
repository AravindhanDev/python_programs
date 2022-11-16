def sumOfSquareNNatural(num):
    return (num * (num + 1) * ((2 * num) + 1)) / 6

num = int(input("Enter number: "))
res = sumOfSquareNNatural(num)
print(int(res))
