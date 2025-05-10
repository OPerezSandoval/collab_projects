
# We can start with building the simple logic of this.
# For instance setting up a list with a few words the amount of attempts the
# user has based on the size of the word. Maybe an input start screen.
# Once logic is set, we can integrate the ascii art portion.

import random

# List of words & a random selection
word_bank = ["pizza", "documents", "computer", "jellyfish", "hi", "secret"]
word = random.choice(word_bank)

# Attempts to user based on word length
attempts = 0

if len(word) < 5:
    user_attempts = 4
else:
    user_attempts = 10

print(user_attempts)




print(word)
