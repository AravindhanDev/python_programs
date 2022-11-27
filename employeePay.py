def calculateEmployeesTotalWeeklyPay(totalRegularHours, hourlyWages, totalOverTimeHours):
    return (totalRegularHours * hourlyWages) + (totalOverTimeHours * (1.5 * hourlyWages))


workingDaysPerWeek = int(input("Working days per week "))
totalRegularHours = int(input("Regular hours ")) * workingDaysPerWeek
hourlyWages = int(input("Hourly wages "))
totalOverTimeHours = int(input("Total Over Time Hours"))
employeesTotalWeeklyPay = calculateEmployeesTotalWeeklyPay(totalRegularHours, hourlyWages, totalOverTimeHours)
print(employeesTotalWeeklyPay)


