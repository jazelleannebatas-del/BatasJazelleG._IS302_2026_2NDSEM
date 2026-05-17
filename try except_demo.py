try:
    number_jab = int(input("Enter a number: "))
    result_jab = 100 / number_jab
    print("Result:", result_jab)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")