while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero")
            continue
        else:
            result = num1 / num2
    else:
        print("Invalid operation")
        continue

    print(f"Result: {result}")
    
    again = input("Do you want to perform another calculation? (y/n): ").lower()
    if again != 'y':
        break