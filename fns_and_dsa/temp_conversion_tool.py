FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    result = (FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit) - 32
    return result

def convert_to_fahrenheit(celsius):
    result = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return result

temperature = int(input("Enter the temperature to convert: "))
user_input_validation = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower().strip()
if user_input_validation == 'f':
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temperature}°C")

elif user_input_validation == 'c':
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temperature}°F")
else:
    print("input, select c or f")
