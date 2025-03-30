import math
# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function for square root
def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number is not possible."
    else:
        return math.sqrt(x)

# Function for exponentiation (Power)
def power(x, y):
    return x ** y

# Function for sine
def sine(x):
    return math.sin(math.radians(x))

# Function for cosine
def cosine(x):
    return math.cos(math.radians(x))

# Function for tangent
def tangent(x):
    return math.tan(math.radians(x))

# Function for the menu display
def display_menu():
    print("\n********* MENU *********")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")
    print("*************************")

def calculator():
    while True:
        # Displaying menu
        display_menu()
        
        # Taking the user's choice
        choice = input("Enter choice (0-9): ")

        # Exit condition
        if choice == '0':
            print("Exiting the Calculator. Goodbye!")
            break

        # Perform operations based on the user's choice
        if choice in ['1', '2', '3', '4', '6']:
            try:
                num1 = float(input("Enter first number: "))
                if choice != '5':  # For square root, only one input is needed
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

        if choice == '1':
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of division is: {divide(num1, num2)}")
        elif choice == '5':
            try:
                num = float(input("Enter number: "))
                print(f"The square root of {num} is: {square_root(num)}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '6':
            print(f"The result of {num1} raised to the power of {num2} is: {power(num1, num2)}")
        elif choice == '7':
            try:
                angle = float(input("Enter angle in degrees: "))
                print(f"The sine of {angle} degrees is: {sine(angle)}")
            except ValueError:
                print("Invalid input! Please enter a valid angle.")
        elif choice == '8':
            try:
                angle = float(input("Enter angle in degrees: "))
                print(f"The cosine of {angle} degrees is: {cosine(angle)}")
            except ValueError:
                print("Invalid input! Please enter a valid angle.")
        elif choice == '9':
            try:
                angle = float(input("Enter angle in degrees: "))
                print(f"The tangent of {angle} degrees is: {tangent(angle)}")
            except ValueError:
                print("Invalid input! Please enter a valid angle.")
        else:
            print("Invalid choice! Please select a valid option from the menu.")

# Run the calculator
calculator()
