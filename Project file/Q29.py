def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        quotient = num1 / num2
        print("Quotient:", quotient)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

divide_numbers()
