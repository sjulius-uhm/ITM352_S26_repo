# Lab on Expressions
# Question 2.1

print("Lab 2: Expressions")
print("\nQuestion 2.1")

# Enter a whole number between 1 and 100
number = int(input("Enter a whole number between 1 and 100: "))  # Prompt user for input
print("You entered:", number)  # Display the entered number

# Calculate the square of the number
square = number ** 2  # Expression to calculate square
print("The square of", number, "is", square)  # Display the square

# Question 2.2

print("\nQuestion 2.2")

# Enter the year you were born as a four-digit number
birth_year = int(input("Enter the year you were born (four-digit number): "))  # Prompt user for birth year
current_year = 2026  # Current year
age = current_year - birth_year  # Expression to calculate age
print(f"Based on the year {birth_year}, you are {age} years old.")  # Display the calculated age

# Question 2.3 and 2.4

print("\nQuestion 2.3 and 2.4")

# Enter a decimal formatted number between 1 and 100 rounded to two decimal places
decimal_number = round(float(input("Enter a decimal number between 1 and 100: ")), 2)  # Prompt user for decimal number
print("You entered:", decimal_number)  # Display the entered decimal number

# Calculate the square of the decimal number to two decimal places
decimal_square = round(decimal_number ** 2, 2)  # Expression to calculate square and round to two decimal places
print("The square of", decimal_number, "is", decimal_square)  # Display the square of the decimal number

# Question 2.5

print("\nQuestion 2.5")

# Determine how many characters are in a sentence of your choice
sentence = input("Enter a sentence of your choice: ")  # Prompt user for a sentence
char_count = len(sentence)  # Expression to count characters in the sentence
print("The number of characters in your sentence is:", char_count)  # Display the character count

# Question 2.6

print("\nQuestion 2.6")

# Enter a weight in pounds and convert to kilograms
weight_pounds = float(input("Enter a weight in pounds: "))  # Prompt user for weight in pounds
weight_kg = round(weight_pounds * 0.453592, 2)  # Expression to convert pounds to kilograms and round to two decimal places
print(f"{weight_pounds} pounds is equal to {weight_kg} kilograms.")  # Display the converted weight

# Question 2.7

print("\nQuestion 2.7")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(temp_f):
    return (temp_f  - 32) * 5.0 / 9.0  # Function to convert Fahrenheit to Celsius

# Test the function with user input
temp_f = float(input("Enter a temperature in Fahrenheit: "))  # Prompt user for temperature in Fahrenheit
temp_c = fahrenheit_to_celsius(temp_f)  # Call the conversion function
print(f"{temp_f} degrees Fahrenheit is equal to {temp_c} degrees Celsius.")  # Display the converted temperature
