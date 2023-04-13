
import random

random = random.randint(1, 100)

guesses = []

while True:
    guess = int(input("Guess a number between 1 and 100. "))

    guesses.append(guess)

    if guess == random:
        print("Congratulations! You guessed the correct number in", len(guesses), "guesses!")
        break

    elif guess > random:
        print("Sorry, your number is too high. Try again.")

    else: # Don't need to add "guess < random"
        print("Sorry, your number is too low. Try again.")