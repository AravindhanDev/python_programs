def isLeapYear(year):
    if year % 400 == 0: return "Leap Year"
    if year % 100 == 0: return "Not a leap year"
    if year % 4 == 0: return "Leap Year"
    return "Not a leap year"
    
year = int(input("Enter year "))
message = isLeapYear(year)
print(message)
