import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    
    # Give the player 3 chances to guess the number
    attempts = 3
    
    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts left. Guess the number: "))
        
        if guess == number_to_guess:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts -= 1
        
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

