import random


word_library = ["charm","creeps", "dreamer", "slippers"]

random_word = random.choice(word_library)
word_length = 0
number_of_guesses = 0
failed_guesses = 0
char_list = [] #keeps track of individual characters in the word
good_guesses = [] #keeps track of all worthy characters in order
bad_guesses = [] #keeps track of all unworthy characters

#user_input = input("Enter a single letter to guess:") # stops code t accept user terminal input

for i in random_word: #determines word length
    word_length += 1
    char_list.append(i)
    good_guesses.append("_")

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


while number_of_guesses > failed_guesses:

    for good in good_guesses:
        print(good, end=" ")
    print("\n")

    user_input = input("Enter a single letter to guess:") # stops code and accept user terminal input

    if user_input in char_list and user_input not in good_guesses: # checks user input versus the characters in the word and in guesses
        for index_value, char in enumerate(char_list):
            print(char)
            if char == user_input:
                good_guesses[index_value] = user_input
                print(index_value)
        print("You correctly guessed:", user_input)

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
    elif good_guesses == char_list:
        print("NO HANGING TODAY!")
        print("Thanks for playing!")
        break

    print(failed_guesses)
    print(number_of_guesses)







