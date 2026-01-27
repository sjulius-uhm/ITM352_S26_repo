# Handy library of mathematical functions
# Samantha Julius
# Date: Jan. 27, 2026

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None
    return number ** 0.5

def exponent(base, exp, precision):
    """Calculate the exponentiation of a base raised to exp."""
    result = base ** exp
    rounded_result = round(result, precision)
    return rounded_result