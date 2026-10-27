# Jenna Gomez
# CIS256 17528
# Programming Assignment 4

import random

def word_game():
    # predifined list household items 
    words = ["cat", "plant", "socks", "table", "chair", "stove", "couch"]
    word = random.choice(words).lower()
    guesses = set()
    incorrect_guesses = set()
    max_attempts = 5

# word game title
    print("☼ Word Guessing Game ☼")
    print("Can you guess the word one letter at a time?")
    print(f"You will have {max_attempts} chances to guess the word!")

    while max_attempts > 0:
       word_try = " ".join(
            letter if letter in guesses else "_"
            for letter in word)

       print(f"Word: {word_try}")
       print(f"Incorrect guess: {', '.join(sorted(incorrect_guesses)) or "None"}")
       print(f"Attempts remaming: {max_attempts}")

# correct guess print
       if all(letter in guesses for letter in word):
           print(f"Congrats! You guessed the correct word: {word}")
           return
       
       guess = input("Enter a letter: ").lower().strip()

# error if they put more than one letter for an attempt
       if len(guess) != 1 or not guess.isalpha():
           print("Invalid input. Please enter a single letter at a time.")
           continue

# repeated letter guess
       if guess in guesses or guess in incorrect_guesses:
           print("Letter already tried. Please try again")
           continue

#correct guess
       if guess in word:
            guesses.add(guess)
            print(f"You got it! '{guess}' is in the word!")
       else:
            incorrect_guesses.add(guess)
            max_attempts -= 1
            print(f"Awe sorry! '{guess}' is not in the word.")

    print("☺ GAME OVER! You are out of guesses. ☺")
    print(f"The correct word was: {word}")
           
if __name__ == "__main__":
    word_game()