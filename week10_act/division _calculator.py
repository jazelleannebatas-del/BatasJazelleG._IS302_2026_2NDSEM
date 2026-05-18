try:
    num1_jab = float(input("Enter first number: "))
    num2_jab = float(input("Enter second number: "))

    result_jab = num1_jab / num2_jab
    print("Result:", result_jab)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid numeric input")
