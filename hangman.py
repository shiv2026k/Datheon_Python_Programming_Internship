import random

# Evolving ASCII stages for each incorrect guess
ASCII_GALLOWS = [
    """
       +---+

       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |

       |   |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """
]

# Static baseline word bank containing curriculum-compliant words
WORD_BANK = ["PYTHON", "DATHEON", "INTERFACE", "VARIABLE", "AUTOMATION", "INTERNSHIP", "CHATBOT"]

def select_word():
    """Selects a random word from the predefined pool."""
    return random.choice(WORD_BANK).upper()

def display_status(gallows_stage, masked_word, guessed_letters):
    """Prints the current gallows visual, hidden word state, and used letters."""
    print(ASCII_GALLOWS[gallows_stage])
    print(f"Word to guess: {' '.join(masked_word)}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print("-" * 40)

def run_game():
    """Manages core loop, tracking state, inputs, and validation checks."""
    print("=========================================")
    print("Welcome to the Datheon Hangman Console Game!")
    print("=========================================")
    
    secret_word = select_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_mistakes = 6
    
    # Initialize mask tracking string characters
    masked_word = ["_" for _ in secret_word]
    
    while incorrect_guesses < max_mistakes:
        display_status(incorrect_guesses, masked_word, guessed_letters)
        
        # User input capture and conversion
        guess = input("Enter a single letter: ").strip().upper()
        
        # Input sanitation and validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️ Invalid input. Please enter exactly one alphabetical letter.")
            continue
            
        if guess in guessed_letters:
            print(f"\n⚠️ You already tried '{guess}'. Penalty avoided. Pick another letter.")
            continue
            
        guessed_letters.add(guess)
        
        # Check matching criteria
        if guess in secret_word:
            print(f"\n✅ Nice job! '{guess}' is in the word.")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    masked_word[index] = guess
        else:
            print(f"\n❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses += 1
            
        # Evaluation check for complete resolution
        if "_" not in masked_word:
            print(ASCII_GALLOWS[incorrect_guesses])
            print(f"🎉 CONGRATULATIONS! You guessed the word: {secret_word}")
            print("=========================================")
            return
            
    # Defeat execution block
    print(ASCII_GALLOWS[max_mistakes])
    print(f"💥 GAME OVER! You ran out of attempts. The word was: {secret_word}")
    print("=========================================")

if __name__ == "__main__":
    run_game()
