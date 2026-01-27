# Functions in Python Tutorial

# What are functions in Python?
# Functions are reusable blocks of code that perform a specific task.
# They allow you to organize your code into logical units, making it easier to read, maintain, and reuse.

# Why are functions useful?
# 1. Code reusability: Write once, use many times
# 2. Modularity: Break down complex problems into smaller, manageable pieces
# 3. Readability: Make code easier to understand and follow
# 4. Maintainability: Changes to functionality can be made in one place
# 5. Testing: Easier to test individual components

# Simple example of defining and calling a function

# Defining a function
def greet(name):
    """
    This function takes a name as input and prints a greeting.
    """
    print(f"Hello, {name}! Welcome to Python functions.")

# Calling the function
greet("Alice")
greet("Bob")
greet("Charlie")

# Another example with return value
def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    """
    return a + b

# Calling the function and storing the result
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# You can also call it directly in a print statement
print(f"10 + 7 = {add_numbers(10, 7)}")

# Different types of function parameters

# 1. Function with no parameters
def say_hello():
    """
    This function takes no parameters and prints a simple greeting.
    """
    print("Hello! This function has no parameters.")

# Calling the function
say_hello()

# 2. Function with one parameter (we already saw greet() above)
# Let's add another example
def square_number(num):
    """
    This function takes one number and returns its square.
    """
    return num * num

# Calling the function
print(f"5 squared is {square_number(5)}")
print(f"10 squared is {square_number(10)}")

# 3. Function with multiple parameters (we already saw add_numbers() above)
# Let's add another example
def calculate_area(length, width):
    """
    This function takes length and width and returns the area of a rectangle.
    """
    return length * width

# Calling the function
print(f"Area of rectangle 4x6: {calculate_area(4, 6)}")
print(f"Area of rectangle 7x3: {calculate_area(7, 3)}")

# 4. Function with default parameters
def greet_person(name, greeting="Hello"):
    """
    This function takes a name and an optional greeting (defaults to "Hello").
    """
    print(f"{greeting}, {name}!")

# Calling with both parameters
greet_person("Alice", "Hi")

# Calling with default greeting
greet_person("Bob")

# Another example with default parameters
def power(base, exponent=2):
    """
    This function calculates base raised to the power of exponent (defaults to 2).
    """
    return base ** exponent

# Calling with both parameters
print(f"2^3 = {power(2, 3)}")

# Calling with default exponent
print(f"5^2 = {power(5)}")  # Uses default exponent of 2

# Return Values in Python Functions
# Functions can return different types of data using the 'return' statement
# The return statement ends function execution and sends a value back to the caller

# 1. Function returning a number (integer/float)
def get_maximum(a, b, c):
    """
    This function returns the largest of three numbers.
    """
    return max(a, b, c)

# 2. Function returning a string
def format_name(first_name, last_name):
    """
    This function returns a formatted full name.
    """
    return f"{first_name.title()} {last_name.title()}"

# 3. Function returning a list
def get_even_numbers(start, end):
    """
    This function returns a list of even numbers between start and end (inclusive).
    """
    return [num for num in range(start, end + 1) if num % 2 == 0]

# 4. Function returning a boolean value
def is_adult(age):
    """
    This function returns True if age is 18 or older, False otherwise.
    """
    return age >= 18

# 5. Function returning multiple values (as a tuple)
def get_user_info(name, age, city):
    """
    This function returns multiple pieces of information as a tuple.
    """
    return name, age, city

# Demonstrating the return value examples
print("\n--- Return Value Examples ---")

# Number return
max_value = get_maximum(15, 27, 12)
print(f"The maximum of 15, 27, 12 is: {max_value}")

# String return
full_name = format_name("john", "doe")
print(f"Formatted name: {full_name}")

# List return
even_nums = get_even_numbers(1, 10)
print(f"Even numbers from 1 to 10: {even_nums}")

# Boolean return
adult_status = is_adult(25)
print(f"Is 25 considered an adult? {adult_status}")

adult_status2 = is_adult(16)
print(f"Is 16 considered an adult? {adult_status2}")

# Multiple values return (tuple unpacking)
name, age, city = get_user_info("Alice", 30, "New York")
print(f"User info: Name={name}, Age={age}, City={city}")

# You can also access tuple elements by index
user_tuple = get_user_info("Bob", 25, "Los Angeles")
print(f"User name: {user_tuple[0]}, User city: {user_tuple[2]}")

# Variable Scope in Python Functions
# Variable scope refers to where a variable can be accessed or modified in your code

# Global variables: Defined outside functions, accessible everywhere
# Local variables: Defined inside functions, only accessible within that function

# Global variable example
global_counter = 0

def increment_counter():
    """
    This function tries to modify a global variable (but will cause an error).
    """
    global_counter += 1  # This will cause UnboundLocalError
    print(f"Counter inside function: {global_counter}")

# Local variable example
def calculate_square(number):
    """
    This function creates a local variable that only exists inside the function.
    """
    result = number ** 2  # 'result' is a local variable
    print(f"Square of {number} is {result}")
    return result

# Demonstrating scope
print("\n--- Variable Scope Examples ---")

# Global variable access (read-only)
print(f"Global counter before: {global_counter}")

# This would cause an error if uncommented:
# increment_counter()  # UnboundLocalError: local variable 'global_counter' referenced before assignment

# Correct way to modify global variables
def increment_counter_correct():
    """
    Correct way to modify a global variable using the 'global' keyword.
    """
    global global_counter  # Declare that we're using the global variable
    global_counter += 1
    print(f"Counter inside function: {global_counter}")

increment_counter_correct()
print(f"Global counter after: {global_counter}")

# Local variable demonstration
calculate_square(5)
# print(result)  # This would cause NameError: name 'result' is not defined

# More scope examples
print("\n--- More Scope Examples ---")

# Example 1: Local variable shadows global variable
x = 10  # Global variable

def shadow_example():
    x = 20  # Local variable with same name
    print(f"Local x: {x}")  # Prints 20

shadow_example()
print(f"Global x: {x}")  # Prints 10 (global unchanged)


# Practical Function Examples - Real-World Problem Solving
# These examples demonstrate functions solving common programming tasks

print("\n--- Practical Function Examples ---")

# 1. CALCULATING AREAS - Geometry calculations
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    Formula: area = length × width
    """
    return length * width

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    Formula: area = π × radius²
    """
    import math
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.
    Formula: area = (base × height) / 2
    """
    return (base * height) / 2

def calculate_room_paint_needed(length, width, height, coats=2):
    """
    Calculate paint needed for a room (excluding ceiling).
    Assumes one gallon covers 350 square feet.
    """
    # Calculate wall areas (4 walls)
    wall_area = 2 * (length * height + width * height)
    total_area = wall_area * coats
    gallons_needed = total_area / 350
    return round(gallons_needed, 2)

# Testing area calculations
print("Area Calculations:")
print(f"Rectangle (5x3): {calculate_rectangle_area(5, 3)} sq units")
print(f"Circle (radius 4): {calculate_circle_area(4):.2f} sq units")
print(f"Triangle (base 6, height 4): {calculate_triangle_area(6, 4)} sq units")
print(f"Paint needed for 12x10x8 room: {calculate_room_paint_needed(12, 10, 8)} gallons")

# 2. PROCESSING STRINGS - Text manipulation
def format_phone_number(phone):
    """
    Format a phone number into (XXX) XXX-XXXX format.
    Removes all non-digit characters first.
    """
    # Remove all non-digit characters
    digits_only = ''.join(filter(str.isdigit, phone))

    # Check if we have exactly 10 digits
    if len(digits_only) == 10:
        return f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        return "Invalid phone number format"

def count_words(text):
    """
    Count the number of words in a text string.
    """
    # Split by whitespace and filter out empty strings
    words = [word for word in text.split() if word.strip()]
    return len(words)

def generate_username(first_name, last_name, birth_year):
    """
    Generate a username from first name, last name, and birth year.
    Format: firstinitial + lastname + last2digitsofyear
    """
    first_initial = first_name[0].lower()
    last_name_lower = last_name.lower()
    year_last_two = str(birth_year)[-2:]
    return f"{first_initial}{last_name_lower}{year_last_two}"

def is_palindrome(text):
    """
    Check if a text string is a palindrome (reads same forwards and backwards).
    Ignores case and non-alphanumeric characters.
    """
    # Clean the text: remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# Testing string processing
print("\nString Processing:")
print(f"Formatted phone: {format_phone_number('123-456-7890')}")
print(f"Word count: {count_words('Hello world! This is a test sentence.')}")
print(f"Username: {generate_username('John', 'Doe', 1995)}")
print(f"Is 'radar' a palindrome? {is_palindrome('radar')}")
print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {is_palindrome('A man, a plan, a canal: Panama')}")

# 3. WORKING WITH LISTS - Data processing
def find_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def filter_even_numbers(numbers):
    """
    Return a new list containing only even numbers from the input list.
    """
    return [num for num in numbers if num % 2 == 0]

def find_max_min(numbers):
    """
    Find both the maximum and minimum values in a list.
    Returns a tuple (max, min).
    """
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def group_by_length(words):
    """
    Group words by their length.
    Returns a dictionary where keys are lengths and values are lists of words.
    """
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

# Testing list operations
print("\nList Operations:")
scores = [85, 92, 78, 96, 88, 91]
print(f"Average score: {find_average(scores):.1f}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Even numbers: {filter_even_numbers(numbers)}")

max_val, min_val = find_max_min(scores)
print(f"Max score: {max_val}, Min score: {min_val}")

duplicates_list = [1, 2, 2, 3, 4, 4, 5, 1]
print(f"Without duplicates: {remove_duplicates(duplicates_list)}")

words_list = ["cat", "dog", "bird", "elephant", "ant", "bat"]
grouped = group_by_length(words_list)
print(f"Words grouped by length: {grouped}")

# 4. MATHEMATICAL CALCULATIONS - Advanced math
def calculate_compound_interest(principal, rate, years, compounds_per_year=12):
    """
    Calculate compound interest.
    Formula: A = P(1 + r/n)^(nt)
    """
    amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * years)
    return round(amount, 2)

def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def is_prime(number):
    """
    Check if a number is prime.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two points.
    Formula: distance = sqrt((x2-x1)² + (y2-y1)²)
    """
    import math
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testing mathematical calculations
print("\nMathematical Calculations:")
print(f"Compound interest ($1000 at 5% for 3 years): ${calculate_compound_interest(1000, 0.05, 3)}")

print(f"First 10 Fibonacci numbers: {fibonacci_sequence(10)}")

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 15 prime? {is_prime(15)}")

distance = calculate_distance(0, 0, 3, 4)
print(f"Distance between (0,0) and (3,4): {distance}")

print(f"Factorial of 5: {factorial(5)}")

# Example 2: Accessing global variable inside function (read-only)
def read_global():
    print(f"Reading global x: {x}")  # Can read global variable

read_global()

# Example 3: Modifying global variable correctly
y = 100

def modify_global():
    global y
    y = 200
    print(f"Modified global y to: {y}")

modify_global()
print(f"Global y after modification: {y}")

# Example 4: Nested functions and scope
def outer_function():
    outer_var = "I'm in outer function"

    def inner_function():
        inner_var = "I'm in inner function"
        print(f"Inner can access outer: {outer_var}")
        print(f"Inner variable: {inner_var}")

    inner_function()
    print(f"Outer can access its own: {outer_var}")
    # print(inner_var)  # This would cause NameError

outer_function()

# Best practices for avoiding scope issues:
# 1. Avoid modifying global variables inside functions
# 2. Pass variables as parameters instead
# 3. Return values instead of modifying globals
# 4. Use the global keyword only when absolutely necessary

def good_practice_counter():
    """
    Good practice: Don't use global variables, pass parameters and return values.
    """
    # Instead of using global, accept current value as parameter
    pass  # We'll implement this below

# Best Practices for Writing Good Python Functions
# Following these guidelines makes your code more readable, maintainable, and professional

print("\n--- Best Practices for Writing Good Python Functions ---")

# 1. NAMING CONVENTIONS
print("1. NAMING CONVENTIONS:")

# Good function names (snake_case, descriptive, verbs)
def calculate_total_price(items, tax_rate=0.08):
    """Calculate total price including tax."""
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)

def validate_email_address(email):
    """Check if email address is valid."""
    return "@" in email and "." in email

def process_user_data(data):
    """Process and validate user data."""
    # Function body would go here
    pass

# Bad function names (avoid these)
# def calc(x, y):  # Too vague
# def getData():   # camelCase instead of snake_case
# def do_stuff():  # Too generic

print("* Use snake_case: calculate_total_price")
print("* Start with verbs: calculate, validate, process")
print("* Be descriptive: avoid generic names like 'calc' or 'do_stuff'")

# 2. FUNCTION DOCUMENTATION (Docstrings)
print("\n2. FUNCTION DOCUMENTATION (Docstrings):")

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI) from weight and height.

    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: BMI value rounded to 1 decimal place

    Raises:
        ValueError: If weight or height are not positive numbers

    Examples:
        >>> calculate_bmi(70, 1.75)
        22.9
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers")

    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def format_address(street, city, state, zip_code):
    """
    Format a complete address string.

    Parameters:
        street (str): Street address
        city (str): City name
        state (str): State abbreviation
        zip_code (str): ZIP code

    Returns:
        str: Formatted address
    """
    return f"{street}, {city}, {state} {zip_code}"

print("* Use triple quotes for docstrings")
print("* Include description, parameters, return values, and examples")
print("* Follow Google/Sphinx style for consistency")

# 3. FUNCTION LENGTH AND COMPLEXITY
print("\n3. FUNCTION LENGTH AND COMPLEXITY:")

# Good: Single responsibility, readable
def is_valid_password(password):
    """Check if password meets security requirements."""
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit

# Bad: Too long, does too many things (don't do this)
# def process_user_registration(name, email, password, age):
#     # Validate name
#     # Validate email
#     # Validate password
#     # Check age
#     # Save to database
#     # Send confirmation email
#     # Log the action
#     # Return success/failure
#     pass

print("* Keep functions under 20-30 lines")
print("* Each function should have a single responsibility")
print("* Break complex functions into smaller helper functions")

# 4. PARAMETER DESIGN
print("\n4. PARAMETER DESIGN:")

# Good: Use default parameters for optional values
def send_email(to_address, subject, body="", priority="normal"):
    """Send an email with optional body and priority."""
    print(f"Sending email to {to_address}")
    print(f"Subject: {subject}")
    if body:
        print(f"Body: {body}")
    print(f"Priority: {priority}")

# Good: Use *args for variable number of arguments
def calculate_average(*numbers):
    """Calculate average of any number of values."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Good: Use **kwargs for optional named parameters
def create_user(name, email, **user_info):
    """Create a user with additional optional information."""
    user = {
        "name": name,
        "email": email
    }
    user.update(user_info)
    return user

print("* Use default parameters for optional values")
print("* Use *args for variable positional arguments")
print("* Use **kwargs for variable keyword arguments")
print("* Avoid too many parameters (max 4-5)")

# 5. ERROR HANDLING
print("\n5. ERROR HANDLING:")

def divide_numbers(dividend, divisor):
    """
    Divide two numbers safely.

    Args:
        dividend (float): Number to be divided
        divisor (float): Number to divide by

    Returns:
        float: Result of division

    Raises:
        ValueError: If divisor is zero
        TypeError: If inputs are not numbers
    """
    try:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both dividend and divisor must be numbers")
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

print("* Use try-except blocks for error handling")
print("* Raise appropriate exceptions with clear messages")
print("* Document exceptions in docstrings")

# 6. CODE ORGANIZATION AND STYLE
print("\n6. CODE ORGANIZATION AND STYLE:")

# Good: Clear variable names and structure
def process_student_grades(grades_list):
    """
    Process a list of student grades and return statistics.
    """
    if not grades_list:
        return {"count": 0, "average": 0, "highest": 0, "lowest": 0}

    total = sum(grades_list)
    count = len(grades_list)
    average = total / count
    highest = max(grades_list)
    lowest = min(grades_list)

    return {
        "count": count,
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest
    }

# Good: Use type hints (Python 3.5+)
from typing import List, Dict, Union

def filter_positive_numbers(numbers: List[float]) -> List[float]:
    """Return only positive numbers from a list."""
    return [num for num in numbers if num > 0]

def get_user_profile(user_id: int) -> Union[Dict, None]:
    """Get user profile by ID, return None if not found."""
    # Implementation would go here
    return None

print("* Use clear, descriptive variable names")
print("* Follow PEP 8 style guidelines")
print("* Use type hints for better code documentation")
print("* Organize code with logical grouping and spacing")

# 7. TESTING AND VALIDATION
print("\n7. TESTING AND VALIDATION:")

def is_leap_year(year):
    """Check if a year is a leap year."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# Test the function
def test_is_leap_year():
    """Test cases for leap year function."""
    assert is_leap_year(2020) == True   # Divisible by 4
    assert is_leap_year(1900) == False  # Divisible by 100 but not 400
    assert is_leap_year(2000) == True   # Divisible by 400
    assert is_leap_year(2021) == False  # Not divisible by 4
    print("All leap year tests passed!")

print("* Write test functions to validate your code")
print("* Test edge cases and error conditions")
print("* Use assertions or testing frameworks like pytest")

# Demonstrating the best practices
print("\n--- Demonstrating Best Practices ---")

# Test the documented functions
bmi = calculate_bmi(70, 1.75)
print(f"BMI for 70kg, 1.75m: {bmi}")

address = format_address("123 Main St", "Springfield", "IL", "62701")
print(f"Formatted address: {address}")

password_valid = is_valid_password("MySecure123")
print(f"Password 'MySecure123' is valid: {password_valid}")

avg = calculate_average(10, 20, 30, 40, 50)
print(f"Average of numbers: {avg}")

user = create_user("John Doe", "john@example.com", age=30, department="IT")
print(f"Created user: {user}")

result = divide_numbers(10, 2)
print(f"10 ÷ 2 = {result}")

grades_stats = process_student_grades([85, 92, 78, 96, 88])
print(f"Grade statistics: {grades_stats}")

positive_nums = filter_positive_numbers([-2, 5, -8, 10, 3, -1])
print(f"Positive numbers: {positive_nums}")

test_is_leap_year()

# End of copilot examples
print("\n--- End of Copilot Examples ---\n")

print("Part 2: Creating Your First Functions")
# Create 4 different functions based on Copilot's examples.
# Samantha Julius
# Jan. 26, 2026

def multiply_numbers(x, y):
    """This function takes two numbers and returns their product."""
    return x * y

def introduce_yourself(name, age):
    """This function introduces a person with their name and age."""
    return f"My name is {name} and I am {age} years old."

def fahrenheit_to_celsius(fahrenheit):
    """This function converts a temperature from Fahrenheit to Celsius."""
    celsius_value = (fahrenheit - 32) * 5/9
    celsius_value_rounded = round(celsius_value, 1)
    return celsius_value_rounded

def calculate_circle_area(radius, pi=3.14):
    """This function calculates the area of a circle given its radius. Pi defaults to 3.14."""
    return pi * (radius ** 2)

print(f"3 * 4 = {multiply_numbers(3, 4)}")
print(introduce_yourself("Samantha", 25))
print(f"100°F in Celsius is {fahrenheit_to_celsius(100)}°C")
print(f"Area of circle with radius 5: {calculate_circle_area(5)}")

print("\nPart 3: Return Values and Function Output")
# Write 3 functions that return different types of values.
# Samantha Julius
# Jan. 26, 2026

def get_minimum(a, b, c):
    """This function returns the smallest of three numbers."""
    return min(a, b, c)

def format_address(street, city, state, zip_code):
    """This function returns a formatted address string."""
    return f"{street}, {city}, {state} {zip_code}"

def is_even(number):
    """This function returns True if the number is even, False otherwise."""
    return number % 2 == 0

print(f"The minimum of 8, 3, 5 is: {get_minimum(8, 3, 5)}")
print(format_address("123 Main St", "Springfield", "IL", "62701"))
print(f"Is 10 even? {is_even(10)}")

print("\nPart 4: Function Scope and Variables")
# Create examples that demonstrate local vs global scope.
# Samantha Julius
# Jan. 26, 2026

global_var = "I am a global variable"
def demonstrate_scope():
    """This function demonstrates local vs global variable scope."""
    local_var = "I am a local variable"
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable
demonstrate_scope()
# print(local_var)  # This would cause an error: NameError
def modify_global_variable():
    """This function modifies a global variable using the global keyword."""
    global global_var
    global_var = "I have been modified globally"
modify_global_variable()
print(global_var)  # Shows modified global variable

def nested_function_example():
    """This function demonstrates nested functions and scope."""
    outer_var = "Outer variable"
    def inner_function():
        inner_var = "Inner variable"
        print(outer_var)  # Accessing outer function's variable
        print(inner_var)  # Accessing inner function's variable
    inner_function()
    print(outer_var)  # Accessing outer function's variable
    # print(inner_var)  # This would cause an error: NameError
nested_function_example()

print("\nPart 5: Practical Function Examples")
# Implement at least 3 practical functions suggested by Copilot.
# Samantha Julius
# Jan. 26, 2026

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def format_phone_number(phone):
    """Format a phone number into (XXX)XXX-XXXX format."""
    digits_only = ''.join(filter(str.isdigit, phone))
    if len(digits_only) == 10:
        return f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        return "Invalid phone number format"
    
def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print(f"Area of rectangle 5x10: {calculate_rectangle_area(5, 10)} sq units")
print(f"Formatted phone: {format_phone_number('012-345-6789')}")
print(f"Is 29 prime? {is_prime(29)}")

print("\n--- End of Tutorial Parts ---\n")

print("Assessment Challenge")
# Create a function that calculates the area of a rectangle.
# Create a function that determines if a number is even or odd.
# Create a function that takes a list and returns the largest number.
# Create a function with default parameters for greeting users.
# Ensure proper documentation (docstrings) for each function.
# Samantha Julius
# Jan. 26, 2026

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def is_even_or_odd(number):
    """Determine if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

def find_largest_number(numbers):
    """Return the largest number from a list."""
    if not numbers:
        return None
    return max(numbers)

def greet_user(name, greeting="Hello"):
    """Greet a user with a custom or default greeting."""
    return f"{greeting}, {name}!"

print(f"Area of rectangle 7x4: {calculate_rectangle_area(7, 4)} sq units")
print(f"10 is {is_even_or_odd(10)}")
print(f"Largest number in [3, 5, 2, 8, 1]: {find_largest_number([3, 5, 2, 8, 1])}")
print(greet_user("Alice"))
print(greet_user("Bob", "Welcome"))

print("\n--- End of Assessment Challenge ---\n")

print("End of Lab 3 - Functions Tutorial")