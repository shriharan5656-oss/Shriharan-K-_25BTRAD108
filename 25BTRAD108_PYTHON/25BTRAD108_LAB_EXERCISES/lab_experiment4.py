print("SIMPLE CALCULATOR")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose an operation: "))

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

if choice == 1:
    print("Result =", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    if b == 0:
        print("Division by zero is not possible")
    else:
        print("Result =", a / b)

else:
    print("Invalid choice”)
