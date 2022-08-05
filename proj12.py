from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def difficulty_type(difficulty_level):
    if difficulty == "easy":
        return 10
    else:
        return 5

count = difficulty_type(difficulty)
print(f"You have {count} attempts remaining to guess the number.")

can_guess = True
while can_guess:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        can_guess = False
    else:
        if guess < number:
            print("Too low.")
            count -= 1
        else:
            print("Too high.")
            count -= 1
        if count == 0:
            print("You've run out of guesses, you lose.")
            can_guess = False
            break
        else:
            print("Guess again.")
        print(f"You have {count} attempts remaining to guess the number.")
    
