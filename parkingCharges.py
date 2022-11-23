print("Press 1 for Truck/Bus")
print("Press 2 for Car")
print("Press 3 for Cycle/Motor Cycle/Scooter")
vehicle = int(input("Enter option: "))
enteringHour = int(input("Entering hour: "))
enteringMinute = int(input("Entering minute: "))
leavingHour = int(input("Leaving hour: "))
leavingMinute = int(input("Leaving minute: "))

def calculateCharges(timeDiff):
    if timeDiff < 3 and vehicle == 1: return 20
    if timeDiff < 3 and vehicle == 2: return 10
    if timeDiff < 3 and vehicle == 3: return 5
    if timeDiff > 3 and vehicle == 1: return 30
    if timeDiff > 3 and vehicle == 2: return 20
    if timeDiff > 3 and vehicle == 3: return 10

def calculateTimeDifferences(enteringHour, enteringMinute, leavingHour, leavingMinute):
    enteringHour = enteringHour + (enteringMinute / 60)
    leavingHour = leavingHour + (leavingMinute / 60)
    if enteringHour > leavingHour: return (24 - enteringHour)  + leavingHour
    return leavingHour - enteringHour

timeDiff = calculateTimeDifferences(enteringHour, enteringMinute, leavingHour, leavingMinute)
charges = calculateCharges(timeDiff)
print(f'Charages {charges}')
