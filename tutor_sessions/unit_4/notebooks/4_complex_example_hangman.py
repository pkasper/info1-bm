# coding: utf-8

# Load words into a set
word_list = open('words.txt', 'r')

words = []

for line in word_list:
    words.append(line.strip())

word_list.close()


# Select a random word

import random
selected_word = random.choice(words)
# make it lower case so we don't have to worry about cases
selected_word = selected_word.lower()


# Set up game tracking variables

correct_letters = [False] * len(selected_word)
guessed_letters = []
current_word = ['_'] * len(selected_word)
wrong_letters_count = 0


# Ask player for character input

while wrong_letters_count < 7 and False in correct_letters:
    
    # ask the user to enter a letter
    letter = input('Guess a letter: ')
    letter = letter.lower()
    
    # only one letter at a time!
    while (len(letter) is not 1):
        letter = input('Guess one letter only: ')
        letter = letter.lower()
    
    # has this letter already been guessed before? Only continue if it hasn't
    if letter not in guessed_letters:
        
        # the word contain the player's letter!
        if letter in selected_word:
            # now where do we find the letter? We're not using find() because it only finds the first occurrence
            for i in range(len(selected_word)):
                if selected_word[i] == letter:
                    # this letter was guessed correctly, so let's set that position to True
                    correct_letters[i] = True
                    
                    # show the player the current status by showing all correct letters in the word
                    current_word[i] = selected_word[i]
            # the known letters are in a list, so to print them correctly, they need to be joined to a string
            print('This is what you know so far: ' + ' '.join(current_word))
        
        # it doesn't contain the letter
        else:
            # that means one attempt less available...
            wrong_letters_count += 1
            print('Sorry, my word does not contain ' + letter + '. You have ' + str(7 - wrong_letters_count + 1) + ' guesses remaining.')

    # this letter cannot be used anymore
    guessed_letters.append(letter)

# the word has not been guessed but all guesses are used up - the player lost
if False in correct_letters:
    print('Sorry, you lost.')

# everything was guessed correctly
else:
    print('Yay, you won!')



