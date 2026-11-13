import random

secret = random.randint(1, 50)
attempts = 0
print("Guess the hidden number!")
print("The number is between 1 and 50.")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50.")
    elif guess == secret:
        print(f"Correct! You found the number in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
