username = input("Enter username ")
panCardNumber = input("Enter pan card number ")

if username.isalpha() and panCardNumber.isdigit():
    print(f'{username}\'s pan card number is {panCardNumber}')
