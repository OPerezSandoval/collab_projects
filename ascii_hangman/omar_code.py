import random

# Open the texts files and read the output
hangman_text_file = open("hangman_text.txt", "r")
hangman_figures_file = open("hangman_figures.txt", "r")
hangman_text = hangman_text_file.read()
hangman_figures = hangman_figures_file.readlines()
hangman_figures_file.close()
hangman_text_file.close()


# Function to output the hangman character with match case logic
def hangman_character(current_result):
    # For loop will iterate through the specified lines in the txt file.
    match current_result:
        case 0:
            for i in hangman_figures[0:10 - 1]:
                print(i)
        case 1:
            for i in hangman_figures[10 - 1:19 - 1]:
                print(i)
        case 2:
            for i in hangman_figures[19 - 1:28 - 1]:
                print(i)
        case 3:
            for i in hangman_figures[28 - 1:37 - 1]:
                print(i)
        case 4:
            for i in hangman_figures[37 - 1:46 - 1]:
                print(i)
        case 5:
            for i in hangman_figures[46 - 1:55 - 1]:
                print(i)
        case 6:
            for i in hangman_figures[55 - 1:64 - 1]:
                print(i)


# Integrate a menu option for the user
def menu():
    print(hangman_text)
    print("\n__Welcome to Hangman!!__")
    print("________________________\n")
    print("1 - PLAY GAME ")
    print("2 - ADD WORD ")
    print("3 - LEADERBOARD ")
    print("4 - EXIT GRACEFULLY ")

    # Catch the ValueError if selection is not an integer
    try:
        selection = int(input("Please make a selection: "))
        selections = [1, 2, 3, 4]

        # Catch values that are not actual selections
        if selection not in selections:
            print("Please enter a correct value 1,2,3,4!\n")
            menu()
        else:
            # Match the correct selection
            match selection:
                case 1:
                    hangman_game()
                case 2:
                    print("Feature coming soon")
                case 3:
                    print("Feature coming soon")
                case 4:
                    print("You have gracefully left the game, my good sir!")
                    exit()
    except ValueError:
        print("Please enter a correct value 1,2,3,4!\n")
        menu()


def hangman_game():
    # Define the user attempts
    user_attempts = 6
    # Random word selected from list & create a list of the word
    word = str(random.choice(["pie", "documents", "computer", "mouse", "hi"]))
    correct_word = list(word)

    # Keep track of all guessed letters & correct guessed letters
    letters_guessed = str([])
    correct_guessed_letters = []

    # Main code that will run if user has attempts left
    while user_attempts > 0:

        # If the user input letter is in the word, print the letter if not
        # print an underscore.
        for i in word:
            if i in letters_guessed:
                print(i, end="")
            else:
                print("_ ", end="")

        # Ask user for letter input and index only for first letter
        user_guess = str(input(f"\nGuess a letter: "))
        first_letter_user_guess = user_guess[0]

        # Let user know the letter has been guessed
        if first_letter_user_guess in letters_guessed:
            print(f'Whoa there bucko you already guessed: '
                  f'"{first_letter_user_guess}". '
                  f'Use another letter!')

        # Add the users input to the letters_guessed list
        letters_guessed += first_letter_user_guess

        # Keep track of correct letters & exclude duplication in the
        # correct_guessed_letters list. Decrease attempts for incorrect letters
        if first_letter_user_guess in word:
            if first_letter_user_guess not in correct_guessed_letters:
                correct_guessed_letters += first_letter_user_guess
                print(f"You have {user_attempts} attempts remaining.")
                hangman_character(user_attempts)
        else:
            user_attempts -= 1
            print(f"You have {user_attempts} attempts remaining.")
            hangman_character(user_attempts)

        # Compare lengths for the correct word and correct guessed letters
        if len(correct_guessed_letters) == len(correct_word):
            exit(print("You win!"))

    hangman_character(user_attempts)
    exit(print("YOU LOST!!!!"))


# Define the entry point of the script
if __name__ == '__main__':
    menu()
