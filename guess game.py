import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too Low! Try a higher number.")
    elif guess > secret_number:
        print("Too High! Try a lower number.")
    else:
        print("Correct! The number was", secret_number)
        print("You got it in", attempts, "attempts!")
        break