def printStatus(status):
    if status == "S": return "Seperated"
    if status == "M": return "Married"
    if status == "D": return "Divorced"
    if status == "U": return "Unmarried"
    return "Invalid status"

status = printStatus("U")
print(status)
