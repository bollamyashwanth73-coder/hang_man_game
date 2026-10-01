import random

# List of predefined words
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

    # Check if the player has won
    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to the list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game over
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)
