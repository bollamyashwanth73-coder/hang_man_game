import random

# 5 predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Count incorrect guesses
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

    # Check if the player won
    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Make sure only one letter is entered
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# If the player reaches 6 wrong guesses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)
