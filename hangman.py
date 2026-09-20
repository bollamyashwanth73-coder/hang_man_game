
import random

words = ["python", "coding", "computer", "program", "developer"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if "_" not in display_word:
        print("🎉 Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)