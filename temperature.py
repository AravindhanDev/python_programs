def celsiusToFahrenheit(celsius):
    return celsius * (9 / 5) + 32

celsius = float(input("Enter celsius "))
fahrenheit= celsiusToFahrenheit(celsius)
print(f"Fahrenheit = {fahrenheit}")
