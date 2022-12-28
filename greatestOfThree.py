def findGreatestOfThree(number1, number2, number3):
    if number1 > number2 and number1 > number3: return number1
    if number2 > number1 and number2 > number3: return number2
    return number3

greatest = findGreatestOfThree(10, 20, 30)
print(f"Gretest = {greatest}")
