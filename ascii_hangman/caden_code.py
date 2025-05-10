import random


word_library = ["charm","creeps", "dreamer", "slippers"]

random_word = random.choice(word_library)
word_length = 0
number_of_guesses = 0
failed_guesses = 0
char_list = []

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







