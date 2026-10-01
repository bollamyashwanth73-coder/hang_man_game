
import random

# List of 5 predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if player has won
    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    # Get player's guess
    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Player loses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)