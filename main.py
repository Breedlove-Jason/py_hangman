import random
from hangman_words import WORD_BANK

# Hangman Game TODO List

# DONE: Import necessary modules (e.g., random, sys)

# DONE: Implement a function to select a random word from the word bank
def get_random_word(word_list):
    """Select and return a random word from the provided word bank."""
    # DONE: Use the random module to select a word
    return random.choice(word_list)


# DONE: Initialize the game state:
#   - Number of lives (attempts)
#   - The chosen word in a masked form (e.g., underscores for each letter)
#   - List of guessed letters
def initialize_game(chosen_word):
    """
    Set up initial game variables:
    - lives: Number of attempts
    - placeholders: Masked word with underscores for unguessed letters
    - guessed_letters: List for correct guesses (for tracking)
    - missed_letters: List for incorrect guesses
    """
    # DONE: Set up initial game variables
    lives = 6
    guessed_letters = []
    missed_letters = []
    masked_word = "_ " * len(chosen_word)

    return lives, masked_word, guessed_letters, missed_letters

#DONE: Write a function to display the current game progress
#   - Show the masked word with correctly guessed letters
#   - Display guessed letters and remaining lives
def display_progress(masked_word, guessed_letters, missed_letters, lives):
    # DONE: Format and print the current game state
    """Display the current game progress."""
    print("\nCurrent game status:")
    print(f"Word: {masked_word}")
    print(f"Guessed letters: {guessed_letters}")
    print(f"Missed letters: {missed_letters}")
    print(f"Lives remaining: {lives}\n")


#DONE: Write a function to handle user input (guessing a letter or the entire word)
def get_user_guess():
    # DONE: Validate input (e.g., ensure single letter input or valid word guess)
    guess = input("Enter a letter or the entire word: ").lower()
    return guess


# DONE: Write a function to update the game state based on the user's guess
#   - Check if the guessed letter/word is in the chosen word
#   - Update the masked word and lives accordingly


def update_game_state(guess, chosen_word, masked_word, lives, guessed_letters, missed_letters):
    """
    Update the game state based on the user's guess.
    For a single letter guess, update placeholders and record the guess.
    For a full word guess, check for correctness.
    Returns the updated masked word and lives.
    """
    if len(guess) == 1:
        if guess in guessed_letters or guess in missed_letters:
            print(f"You already guessed {guess}. Try again.")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            masked_word = "".join([letter if letter in guessed_letters else "_" for letter in chosen_word])
            print(f"Good job! '{guess}' is in the word.")
        else:
            missed_letters.append(guess)
            print(f"Sorry, '{guess}' is not in the word.")
            lives -= 1
    else:
        if guess == chosen_word:
            masked_word = chosen_word
            print(f"Good job! You guessed the word {chosen_word}!")
        else:
            print(f"Sorry, {guess} is not the word.")
            lives -= 1
    return masked_word, lives


# DONE: Write a function to determine if the game has been won or lost
def check_game_over(masked_word, lives):
    """
    Check if the game is over.
    Returns a tuple (game_over_flag, message).
    """
    # DONE: Return a flag for game win or loss, and possibly a message
    if lives > 0 and "_" not in masked_word:
        return True, "Congratulations! You won!"
    elif lives == 0:
        return True, "Game over! You lost!"
    return False, ""


# DONE: Implement a function to display hangman ASCII art based on the number of remaining lives
def display_hangman(lives):
    # DONE: Create a list/dictionary of hangman stages and print the appropriate stage
    """
    Display hangman ASCII art based on the number of remaining lives.
    The stages progress as the player makes incorrect guesses.
    """
    hangman_stages = [
        # Stage 0: No wrong guesses
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        # Stage 1: 1 wrong guess
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        # Stage 2: 2 wrong guesses
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        # Stage 3: 3 wrong guesses
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        # Stage 4: 4 wrong guesses
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        # Stage 5: 5 wrong guesses
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        # Stage 6: 6 wrong guesses (final stage)
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """,
    ]
    index = 6 - lives if lives >= 0 else 6
    print(hangman_stages[index])

# DONE: Write the main game loop
def main():
    # DONE: Initialize the game variables
    # DONE: Loop until the game is over:
    #       - Display progress
    #       - Get user guess
    #       - Update game state
    #       - Display hangman art (if applicable)
    # DONE: Display win/lose message and ask if the player wants to play again
    play_again = True
    while play_again:
        chosen_word = get_random_word(WORD_BANK)
        lives, placeholders, guessed_letters, missed_letters = initialize_game(chosen_word)
        game_over = False
        print(f"Welcome to Hangman! The word has {len(chosen_word)} letters.")
        # Main game loop
        while not game_over:
            display_hangman(lives)
            display_progress(placeholders, guessed_letters, missed_letters, lives)
            guess = get_user_guess()
            placeholders, lives = update_game_state(guess, chosen_word, placeholders, lives, guessed_letters, missed_letters)
            game_over, message = check_game_over(placeholders, lives)
            display_hangman(lives)
            print(message)
            print(f"The word was: {chosen_word}")

        response = input("Do you want to play again? (y/n): ").lower().strip()
        play_again = response == "y"

if __name__ == "__main__":
    main()
