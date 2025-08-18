import random, os, time

# List of possible words for the game
list_of_words = ["apple", "orange", "grapes", "pear"]

# Track letters the player has already guessed
letter_picked = []

# Number of allowed incorrect guesses
lives = 6

# Randomly select a word for the game
word = random.choice(list_of_words)

# Main game loop
while True:
    time.sleep(1)
    os.system("clear")  # Clear the terminal screen

    # Ask the player to guess a letter
    letter = input("Choose a letter: ").lower()

    # If letter already guessed, notify and skip this round
    if letter in letter_picked:
        print("You've tried that before")
        continue

    # Add letter to list of guessed letters
    letter_picked.append(letter)

    # Check if guessed letter is in the word
    if letter in word:
        print("You found a letter")
    else:
        print("Nope, not in there")
        lives -= 1  # Lose a life

    # Display the current guessed state of the word
    all_letters = True
    print()
    for i in word:
        if i in letter_picked:
            print(i, end="")  # Show correct letter
        else:
            print("_", end="")  # Hide unguessed letter
            all_letters = False
    print()

    # Check for win condition
    if all_letters:
        print(f"You won with {lives} left!")
        break

    # Check for lose condition
    if lives <= 0:
        print(f"You ran out of lives! The answer was {word}")
        break
    else:
        print(f"Only {lives} left")  # Show remaining lives