def checkLeapYear(year):
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False

year = int(input("Enter year: "))
res = checkLeapYear(year)

if res == True:
    print("Leap year")
else:
    print("Not a leap year")
