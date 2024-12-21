import random
from words import words  # Make sure 'words' file is in the same folder as this code
import string

def get_valid_word(words):
    word = random.choice(words)  # Randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def display_word(word, used_letters):
    # Display the word with guessed letters visible and underscores for unguessed letters
    return ''.join([letter if letter in used_letters else '_' for letter in word])

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user
    attempts_left = 6  # Number of incorrect attempts allowed

    print("Welcome to Hangman!")
    print(display_word(word, used_letters))

    while attempts_left > 0 and word_letters:
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good guess! {display_word(word, used_letters)}")
            else:
                attempts_left -= 1
                print(f"Wrong guess! You have {attempts_left} attempts left. {display_word(word, used_letters)}")
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if word_letters:
        print(f"You lost! The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word: {word}")

# Run the game
hangman()
