import random


word_library = ["charm","creeps", "dreamer", "slippers"]

random_word = random.choice(word_library)
word_length = 0
number_of_guesses = 0
failed_guesses = 0
char_list = []
good_guesses = []
bad_guesses = []

#user_input = input("Enter a single letter to guess:") # stops code t accept user terminal input

for i in random_word: #determines word length
    word_length += 1
    char_list.append(i)

if word_length <= 4:
    number_of_guesses = 4

elif word_length <= 6:
    number_of_guesses = 5

elif word_length >= 8:
    number_of_guesses = 6


print("-------------------------------")
print("-------------------------------")
print("-- Welcome To Brutal Hangman --")
print("-------------------------------")
print("--        GOOD LUCK!         --")
print("-------------------------------")
print("\n")

for i in char_list:
    print("_", end="")
print("\n")

while number_of_guesses > failed_guesses:

    user_input = input("Enter a single letter to guess:") # stops code and accept user terminal input

    if user_input in char_list and user_input not in good_guesses: # checks user input versus the characters in the word and in guesses
        good_guesses.append(user_input)
        print("You correctly guessed:", user_input)
        print(char_list.index(user_input))
    elif user_input in char_list and user_input in good_guesses:
        print("You have already guessed this letter.")
    elif user_input not in char_list and user_input not in bad_guesses:
        bad_guesses.append(user_input)
        failed_guesses += 1
        print("Bad guess, try again.")
    elif user_input not in char_list and user_input in bad_guesses:
        print("This was already a failed guess.")

    if failed_guesses == number_of_guesses:
        print("YOU ARE A FAILURE!")
        break

    print(failed_guesses)
    print(number_of_guesses)







