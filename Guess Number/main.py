from random import randint
from art import logo

EASY = 10
HARD = 5

def evaluate_guess(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY
    else:
        return HARD
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    attempts = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))
        attempts = evaluate_guess(guess, answer, attempts)
        
        if attempts == 0 and guess != answer:
            print("You've run out of attempts. You lose.")
            print(f"The correct answer was {answer}.")
            return
        
game()