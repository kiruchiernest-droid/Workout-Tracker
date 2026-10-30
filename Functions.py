import math
while True:
    print("\n1. Add\n2. Subtract\n3. multiply\n4. square_root\n5. Divide\n6. Power\n7. exit")

    choice = input("Choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a + b)

    elif choice == "2":
        a = float(input("Eneter first number: "))
        b = float(input("Enter second number: "))
        print(a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a * b)

    elif choice == "4":
        a = float(input("Enter first number:"))
        if a < 0:
            print("Error cannot take a sqrt of a negative number: ")
        else:
            print(math.sqrt(a))

    elif choice == "5":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Cannot divide by zero. ")
        else:
            print(a/ b)

    elif choice == "6":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a ** b)
                

    else:
     print("Goodbye. ")
    break
   
