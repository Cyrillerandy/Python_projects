# imports
from hangman_art import stages, logo
from hangman_words import word_list
from IPython.display import clear_output
import random

# pick a random word from a list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# set the number of chances and loop exit condition
end_of_game = False
lives = 6

# print the logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create a list to hold the blanks
display = ['_'] * word_length

# loop until the game ends
while not end_of_game:
    # ask user to guess a letter
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You already guessed {guess}. Pick a different letter.\n')

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # if the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You guessed {guess}. It\'s not in the word. You lost one life.\n')
        lives -= 1
        print(f'Lives remaining: {lives}.\n')
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the hangman art 
    print(stages[lives])

    # clear output for better user experience
    clear_output(wait = True)