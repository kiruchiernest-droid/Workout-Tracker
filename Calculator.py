import math

# FUNCTIONS
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

# MAIN PROGRAM
print("===== KIRUCHI CALCULATOR =====")
memory = 0

while True:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("6. Power")
    print("7. Square Root")
    print("8. Memory")

    choice = input("Choose an operation (1-8): ")

    if choice == "5":
        print("Goodbye!")
        break

    num1 = float(input("Enter first number: "))

    if choice != "7" and choice != "8":  # Only ask second number when needed
        num2 = float(input("Enter second number: "))

    # CALCULATE RESULT
    if choice == "1":
        result = add(num1, num2)
        print("Result:", result)
        memory = result

    elif choice == "2":
        result = subtract(num1, num2)
        print("Result:", result)
        memory = result

    elif choice == "3":
        result = multiply(num1, num2)
        print("Result:", result)
        memory = result

    elif choice == "4":
        result = divide(num1, num2)
        print("Result:", result)
        memory = result if isinstance(result, float) else memory

    elif choice == "6":
        result = power(num1, num2)
        print("Result:", result)
        memory = result

    elif choice == "7":
        result = square_root(num1)
        print("Result:", result)
        memory = result

    elif choice == "8":
        print("Memory:", memory)

    else:
        print("Invalid choice. Try again.")