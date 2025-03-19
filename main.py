import random

# Hangman Game TODO List

# DONE: Import necessary modules (e.g., random, sys)

# TODO: Create a word bank (list of words) for the game
WORD_BANK = [
    "python",
    "java",
    "kotlin",
    "javascript",
    "typescript",
    "swift",
    "objective",
    "ruby",
    "perl",
    "haskell",
    "scala",
    "elixir",
    "rust",
    "go",
    "dart",
    "csharp",
    "cplusplus",
    "php",
    "html",
    "css",
]


# DONE: Implement a function to select a random word from the word bank
def get_random_word(word_list):
    # DONE: Use the random module to select a word
    return random.choice(word_list)


# TODO: Initialize the game state:
#   - Number of lives (attempts)
#   - The chosen word in a masked form (e.g., underscores for each letter)
#   - List of guessed letters
def initialize_game(chosen_word):
    # TODO: Set up initial game variables
    lives = 0
    guessed_letters = []
    missed_letters = []
    placeholders = ""
    for letter in chosen_word:
        placeholders += "_"


# TODO: Write a function to display the current game progress
#   - Show the masked word with correctly guessed letters
#   - Display guessed letters and remaining lives
def display_progress(masked_word, guessed_letters, missed_letters, lives):
    # TODO: Format and print the current game state
    print(f"Guessed letters: {guessed_letters}")
    print(f"Missed letters: {missed_letters}")
    print(f"Lives: {lives}")
    print(f"Word: {masked_word}")


# TODO: Write a function to handle user input (guessing a letter or the entire word)
def get_user_guess():
    # TODO: Validate input (e.g., ensure single letter input or valid word guess)
    guess = input("Enter a letter or the entire word: ").lower()
    return guess


# TODO: Write a function to update the game state based on the user's guess
#   - Check if the guessed letter/word is in the chosen word
#   - Update the masked word and lives accordingly
def update_game_state(guess, chosen_word, masked_word, lives, guessed_letters, missed_letters):
    # TODO: Implement logic for a correct or incorrect guess
    if len(guess) == 1:
        for letter in guessed_letters:
            if letter in chosen_word:
                guessed_letters.append(letter)
                masked_word[letter] = letter
                print(f"Good job! {letter} is in the word.")
                print(f"Guessed letters: {guessed_letters}")
            else:
                missed_letters.append(letter)
                print(f"Sorry, {letter} is not in the word.")
                print(f"Missed letters: {missed_letters}")
                lives += 1


# TODO: Write a function to determine if the game has been won or lost
def check_game_over(masked_word, lives):
    # TODO: Return a flag for game win or loss, and possibly a message
    if lives > 0 and "_" not in masked_word:
        return True, "Congratulations! You won!"


# DONE: Implement a function to display hangman ASCII art based on the number of remaining lives
def display_hangman(lives):
    # DONE: Create a list/dictionary of hangman stages and print the appropriate stage
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
    if lives == 0:
        print(hangman_stages[0])
    elif lives == 1:
        print(hangman_stages[1])
    elif lives == 2:
        print(hangman_stages[2])
    elif lives == 3:
        print(hangman_stages[3])
    elif lives == 4:
        print(hangman_stages[4])
    elif lives == 5:
        print(hangman_stages[5])
    elif lives == 6:
        print(hangman_stages[6])


# TODO: Write the main game loop
def main():
    # TODO: Initialize the game variables
    # TODO: Loop until the game is over:
    #       - Display progress
    #       - Get user guess
    #       - Update game state
    #       - Display hangman art (if applicable)
    # TODO: Display win/lose message and ask if the player wants to play again
    chosen_word = get_random_word(WORD_BANK)
    lives = 0
    guessed_letters = []
    missed_letters = []
    placeholders = ""
    for letter in chosen_word:
        placeholders += "_"
    while True:
        display_hangman(lives)
        get_user_guess()
        display_progress(chosen_word,guessed_letters, missed_letters, lives)
        if check_game_over(placeholders, lives):
            break
        lives += 1
        update_game_state(get_user_guess(), chosen_word, placeholders, lives, guessed_letters, missed_letters)


# TODO: Call the main function to start the game
if __name__ == "__main__":
    main()
