import art
import random
print(art.logo)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Print welcome message and tell the user you are thinking of a number
# between 1 and 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Generate a number between 1 and 100. Random Module can be utilized.
one_and_hundred = int(random.randint(1, 100))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Ask user for difficulty [1] easy or [2] hard.
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
guess = 0
easy_attempts = 10
hard_attempts = 5
# Logic to check if user guess is higher or lower than actual randomly generated number
if difficulty == 'easy':
    while guess != one_and_hundred and easy_attempts != 0:
        guess = int(input("Make a guess: "))
        while guess > one_and_hundred:
            easy_attempts -= 1
            if easy_attempts == 0:
                break
            print("Too high.")
            print(f"You have {easy_attempts} attempts remaining to guess the number.")
            break
        while guess < one_and_hundred:
            easy_attempts -= 1
            if easy_attempts == 0:
                break
            print("Too low.")
            print(f"You have {easy_attempts} attempts remaining to guess the number.")
            break


elif difficulty == 'hard':
    while guess != one_and_hundred and hard_attempts != 0:
        guess = int(input("Make a guess: "))
        if hard_attempts == 0:
            break
        while guess > one_and_hundred:
            hard_attempts -= 1
            if hard_attempts == 0:
                break
            print("Too high.")
            print(f"You have {hard_attempts} attempts remaining to guess the number.")
            break
        while guess < one_and_hundred:
            hard_attempts -= 1
            if hard_attempts == 0:
                break
            print("Too low.")
            print(f"You have {hard_attempts} attempts remaining to guess the number.")
            break


if guess == one_and_hundred:
        print(f"You got it! The answer was {one_and_hundred}")
if hard_attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
if easy_attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
