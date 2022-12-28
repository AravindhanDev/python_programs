def run(number):
    print('first', str(number)[0], 'last', str(number)[-1], 'middle', str(number)[len(str(number))//2])

number = int(input("Enter number "))
run(number)
