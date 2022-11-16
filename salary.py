basicPay = float(input("Enter basic pay "))
HRA = 10
TA = 5

salary = basicPay + (basicPay * (5 / 100)) + (basicPay * (10 / 100))
print("Salary: {}".format(salary))
