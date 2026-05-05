# Ask the user to enter a temperature in Fahrenheit.
# Convert the temperature to Celsius using the formula: C = (F - 32) * 5/9
# Program written as a function.
# Name: Samantha Julius
# Date: January 22, 2026

def fahrenheit_to_celsius(fahrenheit):
    """This function converts a temperature from Fahrenheit to Celsius."""
    celsius_value = (fahrenheit - 32) * 5/9
    celsius_value_rounded = round(celsius_value, 1)
    return celsius_value_rounded

fahrenheit_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheit_value = float(fahrenheit_input)
celsius_value = fahrenheit_to_celsius(fahrenheit_value)

print("You entered: ", fahrenheit_value)
print(f"The temperature in Celsius is: {celsius_value}")