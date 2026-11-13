number = int(input("Enter a number: "))
# Prime number check
if number < 2:
    prime = False
else:
    prime = True
    for value in range(2, number):
        if number % value == 0:
            prime = False
            break

if prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

# Factorial calculation
if number < 0:
    print("Factorial is not available for negative numbers.”)
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial = factorial * value
    print("Factorial =", factorial)
