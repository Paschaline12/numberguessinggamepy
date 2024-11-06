import random
lowest = 1
highest = 100

answer = random.randint(lowest, highest)
guesses = 0
running = True

print("Python Number Guessing Game:")

print(f"Select a number between {lowest} and {highest}")

while running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess= int(guess)
        guesses += 1
        if guess < lowest or guess > highest:
            print("That number is out of range: ")
            print(f"Please input a number between {lowest} and {highest}")

    else:
        print("Invalid Guess")
        print(f"Please input a number between {lowest} and {highest}")
