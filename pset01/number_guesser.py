import random

print("Welcome to the Number Guesser!")
print("Please guess a number between 1 and 1000")
print("Type `bye` or `exit` to quit the program at anytime.")

print()

n = random.randint(1, 1000)
attempts = 0

while True:
    response = input("What is your guess? ").strip().lower()
    if response == "bye" or response == "exit":
        print("Goodbye!")
        exit()
    elif not response.isdigit():
        print("Please enter a valid number")
    elif int(response) > n:
        attempts += 1
        print("Too high!")
    elif int(response) < n:
        attempts += 1
        print("Too low!")
    else:
        attempts += 1
        print("Congratulations! You guessed the number!")
        print(f"It took you {attempts} attempts.")
        print()
        print("I picked a new number between 1 and 1000. Let's play again!")
        n = random.randint(1, 1000)
        attempts = 0