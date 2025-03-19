import random
# Hangman Game TODO List

# DONE: Import necessary modules (e.g., random, sys)

# TODO: Create a word bank (list of words) for the game
WORD_BANK = [
    "python", "java", "kotlin", "javascript", "typescript",
    "swift", "objective", "ruby", "perl", "haskell",
    "scala", "elixir", "rust", "go", "dart",
    "csharp", "cplusplus", "php", "html", "css"
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
    lives = 6
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
    for letter in guessed_letters:
        if letter in masked_word:
            guessed_letters.append(letter)
            masked_word[letter] = letter
            print(f"Good job! {letter} is in the word.")
        else:
            missed_letters.append(letter)
            print(f"Sorry, {letter} is not in the word.")


# TODO: Write a function to handle user input (guessing a letter or the entire word)
def get_user_guess():
    # TODO: Validate input (e.g., ensure single letter input or valid word guess)
    pass

# TODO: Write a function to update the game state based on the user's guess
#   - Check if the guessed letter/word is in the chosen word
#   - Update the masked word and lives accordingly
def update_game_state(guess, chosen_word, masked_word, lives, guessed_letters):
    # TODO: Implement logic for a correct or incorrect guess
    pass

# TODO: Write a function to determine if the game has been won or lost
def check_game_over(chosen_word, masked_word, lives):
    # TODO: Return a flag for game win or loss, and possibly a message
    pass

# TODO: Implement a function to display hangman ASCII art based on the number of remaining lives
def display_hangman(lives):
    # TODO: Create a list/dictionary of hangman stages and print the appropriate stage
    pass

# TODO: Write the main game loop
def main():
    # TODO: Initialize the game variables
    # TODO: Loop until the game is over:
    #       - Display progress
    #       - Get user guess
    #       - Update game state
    #       - Display hangman art (if applicable)
    # TODO: Display win/lose message and ask if the player wants to play again
    pass

# TODO: Call the main function to start the game
if __name__ == "__main__":
    main()
