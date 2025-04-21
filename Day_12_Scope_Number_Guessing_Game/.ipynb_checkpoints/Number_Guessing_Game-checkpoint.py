# imports
from art import logo, goodbye
from IPython.display import clear_output
import random

# create a function for the gameplay
def guess_the_number():
    # choose a number
    chosen_num = random.randint(1, 100) 
    
    # print the game logo and welcome message
    print(logo)
    print('\nWelcome to the Number Guessing Game!')
    print("\nI'm thinking of a number between 1 and 100.")

    # choose a difficulty level
    difficulty = input('\nChoose a difficulty level. Type "easy" or "hard": ').lower()
    # ensure correct difficulty is chosen
    while difficulty not in ['easy', 'hard']:
        difficulty = input('Invalid choice.\nChoose a difficulty level. Type "easy" or "hard": ').lower()

    # set attempts based on difficulty level
    attempts = 0  # a starting number
    
    if difficulty == 'easy':
        attempts += 10
    elif difficulty == 'hard':
        attempts += 5
        
    # loop through the attempts and guess
    while attempts > 0:
        print(f'\nYou have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))

        # check if guess is the chosen number or they're out of guesses
        if attempts == 1 and guess != chosen_num:
            print("You've run out of guesses.")
        elif guess > chosen_num:
            print('Too high.\nGuess again.')
        elif guess < chosen_num:
            print('Too low.\nGuess again.')
        elif guess == chosen_num:
            print(f'You got it right. The answer is {chosen_num}.')
            break

        # reset the attempts
        attempts -= 1

    # restart the game
    if guess == chosen_num or attempts == 0:
        play_game = input('Do you want to play again? Type "yes" or "no": ').lower()
        if play_game == 'yes':
            clear_output()
            guess_the_number()
        else:
            clear_output()
            print(logo)
            print(goodbye)
    
guess_the_number()