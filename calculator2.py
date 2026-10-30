import math

while True:

    print("\n===== ERNEST CALCULATOR ===== ")
    print("1. Addition" )
    print("2. Subtraction ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Square_root ")
    print("6. Exit ") 

    
    choice = input("choose an operation (1-6): ")

    if choice == "1":
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))

        print("Result", a + b)
    
    

    elif choice == "2":
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        print("Result", a - b)

    elif choice == "3":
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        print("Result", a * b)
        
    elif choice == "4":
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        
    
        if b == "0":
         print("error cannot divide by zero")
        else:
         print("Result", a / b )

    elif choice == "5":
     a = float(input("enter number: "))
     print("Result", math.sqrt(a))
    elif choice == "6":
     print("Goodbye Ernest ")
     break
    
    else:
     print("Invalid choice. Try again ")
