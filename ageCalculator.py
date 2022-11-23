from datetime import date

def calculateAge(dob, now):
    age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
    return age

year = int(input("Enter birth year "))
month = int(input("Enter birth month "))
day = int(input("Enter birth day "))

dob = date(year, month, day)
now = date.today()
age = calculateAge(dob, now)
print(f'Date of birth {dob.day}/{dob.month}/{dob.year}')
print(f'Today {now.day}/{now.month}/{now.year}')
print(f'You are {age} years old')

