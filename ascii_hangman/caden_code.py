import random


word_library = ["charm","creeps", "dreamer", "slippers"]

random_word = random.choice(word_library)
word_length = 0
failed_guesses = 0
char_list = [] #keeps track of individual characters in the word
good_guesses = [] #keeps track of all worthy characters in order
bad_guesses = [] #keeps track of all unworthy characters

#user_input = input("Enter a single letter to guess:") # stops code t accept user terminal input

for i in random_word: #determines word length
    word_length += 1
    char_list.append(i)
    good_guesses.append("_")



print("-------------------------------")
print("-------------------------------")
print("-- Welcome To Brutal Hangman --")
print("-------------------------------")
print("--        GOOD LUCK!         --")
print("-------------------------------")


def hangman_status(attempts):
    if attempts == 0:
        print(" _____")
        print("|     |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("______")
    elif attempts == 1:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|")
        print("|")
        print("|")
        print("______")
    elif attempts == 2:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|     |")
        print("|     |")
        print("|")
        print(" ______")
    elif attempts == 3:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|     |/ ")
        print("|     | ")
        print("|")
        print("______")
    elif attempts == 4:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|    \|/ ")
        print("|     |")
        print("|")
        print("______")
    elif attempts == 5:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|    \|/ ")
        print("|     |")
        print("|    / ")
        print("______")
    elif attempts == 6:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|    \|/ ")
        print("|     | ")
        print("|    / \ ")
        print("______")
    return


while 7 > failed_guesses:

    hangman_status(failed_guesses)


    for good in good_guesses:
        print(good, end=" ")
    print("\n")

    user_input = input("Enter a single letter to guess:") # stops code and accept user terminal input
    print("\n")
    if user_input in char_list and user_input not in good_guesses: # checks user input versus the characters in the word and in guesses
        for index_value, char in enumerate(char_list):
            if char == user_input:
                good_guesses[index_value] = user_input

        print("You correctly guessed:", user_input)

    elif user_input in char_list and user_input in good_guesses:
        print("You have already guessed this letter.")

    elif user_input not in char_list and user_input not in bad_guesses:
        bad_guesses.append(user_input)
        failed_guesses += 1
        if failed_guesses < 6:
            print("Bad guess, try again.")

    elif user_input not in char_list and user_input in bad_guesses:
        print("This was already a failed guess.")

    if failed_guesses == 7:
        print("YOU ARE A FAILURE!")
        print("THE MAN HANGED!")
        break
    elif good_guesses == char_list:
        print("")
        hangman_status(failed_guesses)
        print("")
        for good in good_guesses:
            print(good, end=" ")
        print("\n")
        print("NO HANGING TODAY!\n")
        print("Thanks for playing!")
        break








