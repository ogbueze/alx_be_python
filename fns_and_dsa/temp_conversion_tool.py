FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celcius = (fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR ) - 32
    return celcius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


try:
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
except ValueError:
    print("Please enter a valid integer to proceed")
