number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))

def performCalculation(number1, number2):
    print("Addition of", number1, "and", number2, "is", number1 + number2)
    print("Subtraction of", number1, "and", number2, "is", number1 - number2)
    print("Multiplication of", number1, "and", number2, "is", number1 * number2)
    print("Division of", number1, "and", number2, "is", number1 / number2)
    print("Modulo Division of", number1, "and", number2, "is", number1 % number2)
    print("Floor Division of", number1, "and", number2, "is", number1 // number2)
    print("Exponent of", number1, "and", number2, "is", number1 ** number2)

performCalculation(number1, number2)

