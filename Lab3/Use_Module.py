import HandyMath
from HandyMath import max, min

# Ask the user for two numbers and calculate their midpoint.
print("Let's calculate the midpoint between two numbers.")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = HandyMath.midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {result}")

# Ask the user for a number and calculate its square root.
print("\nNow, let's find the square root of a number.")
number_input = float(input("Enter a number to find its square root: "))
result = HandyMath.sqrt(number_input)
if result is None:
     print("Cannot compute the square root of a negative number.")
else:
     print(f"The square root of {number_input} is {result}")

# Ask the user for a base, exponent, and precision to calculate exponentiation.
print("\nNext, let's calculate exponentiation.")
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
precision = int(input("Enter the number of decimal places for precision: "))
result = HandyMath.exponent(base, exponent, precision)
print(f"{base} raised to the power of {exponent} is {result} (rounded to {precision} decimal places)")

# Ask the user for two numbers and find the maximum and minimum.
print("\nFinally, let's find the maximum and minimum of two numbers.")
num1 = float(input("Enter the first number to compare: "))
num2 = float(input("Enter the second number to compare: "))
max_value = max(num1, num2)
min_value = min(num1, num2)
print(f"The maximum number of {num1} and {num2} is {max_value}")
print(f"The minimum number of {num1} and {num2} is {min_value}")