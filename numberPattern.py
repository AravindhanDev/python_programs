number = int(input("Enter number "))
list = []

while number > 0:
    list.append(number % 10)
    number = int(number / 10)

list = list[::-1]

for i in range(len(list)):
    for j in range(i+1):
        print(list[j], end='')
    print("\n")

for i in range(len(list)):
    for k in range(i):
        print(end=' ')

    for j in range(i, len(list)):
        print(list[j], end='')

    print("\n")

