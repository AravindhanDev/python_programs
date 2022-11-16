even = 0
odd = 0
choice = 0

while (choice != -1):
    number = int(input("Enter number: "))
    if number % 2 == 0: even+=1
    else: odd+=1
    choice = int(input("Do you want to continue?: "))

print(odd, even)
