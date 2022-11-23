unit = int(input("Enter consumption unit "))

def calculateBill(unit):
    if unit < 150: return 3 * unit
    if unit < 350: return 100 + (3.75 * unit)
    if unit < 450: return 250 + (4 * unit)
    if unit < 600: return 300 + (4.25 * unit)
    return 400 + (5 * unit)

billAmountToPaid = calculateBill(unit)
print(f'Amount to be paid {billAmountToPaid}')
