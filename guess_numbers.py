import random

secret_number = random.randint(1,100)
attempts = 0

print("Welcome to the number guessing game!")
print("Think of a number between 1 and 100")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low. Try Again")
        elif guess > secret_number:
            print("Too High. Try again")
        else:
            print(f"Correct! You guessed the number in {attempts} tries.")
            break
    except ValueErrors:
        print("Please ener a valid whole number")