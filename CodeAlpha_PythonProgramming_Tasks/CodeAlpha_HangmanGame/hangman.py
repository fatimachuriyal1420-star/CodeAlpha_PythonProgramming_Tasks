# To choose random word
import random 

# List of words
words = ["apple", "banana", "grape", "mango", "peach","orange"]

# Choose random word
word = random.choice(words)

# Store correct guesses
guessed = []  

# Store wrong guesses
wrong_letters = [] 
# Total attempts allowed 
attempts = 6 

print(" Welcome to Hangman Game!")

# Game loop
while attempts > 0:
    display = ""  # To show current word progress

    # Create display word
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())
    print(" Wrong letters:", wrong_letters)
    print(" Attempts left:", attempts)

    # Check win condition
    if "_" not in display:
        print(" Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input(" Guess a letter: ").lower()

    # Input validation (only single letter)
    if len(guess) != 1 or not guess.isalpha():
        print(" Enter only one letter!")
        continue

    # Already guessed check
    if guess in guessed or guess in wrong_letters:
        print(" You already guessed that letter!")
        continue

    # Correct guess
    if guess in word:
        guessed.append(guess)
        print(" Correct guess!")
    else:
        wrong_letters.append(guess)
        attempts -= 1
        print(" Wrong guess!")

# Lose condition
if attempts == 0:
    print("\n Game Over! The word was:", word)