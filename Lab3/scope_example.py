# This program demonstrates variable scope in Python.
# Name: Samantha Julius
# Date: Jan. 27, 2026

def calculates_discounted_price(price, discount):
    price = price * discount
    print(f"Inside function, discounted price: {price:.2f}")
    return price

discount = 0.6
price = 100
print(f"Original price before function call: {price:.2f}")
discounted_price = calculates_discounted_price(price, discount)

print(f"Original price after function call: {price:.2f}")
print("Discount =", discount)