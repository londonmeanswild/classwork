# !/usr/bin/env python3
# (c) Landon A Marchant
# A word game using wordTools

"""This is a word guessing game utilizing wordTools.py.
    
The computer picks a random 4-letter isogram, and the user takes turns trying to guess the word. 
If the user guesses all four letters correctly, they win. If not, the number of correct letters is reported and the game continues.
    
User has fifteen turns to guess the isogram. If user fails to guess the word after fifteen turns, game will print the target word."""

from wordTools import *
from random import random

def main():
    dictionary_words = words()
    dictionary_isograms = isograms(dictionary_words)
    four_letter_words = sized(dictionary_isograms, 4)
    index_of_word = int(random() * len(four_letter_words))
    word_to_guess = four_letter_words[index_of_word].lower()

    print("I have chosen a four-letter word. Try to guess it by typing four letters.")
    turns = 15
    while True:
        user_input = input("Please enter a four letter isogram. You have %i turns: " % 
                           turns)
        if len(user_input) != 4:
            print("That was not a four letter isogram.")
            continue
        
        result = match(word_to_guess, user_input)
        print("Matches: " + str(result[0]))
        if result[0] == 4:
            print("You so smart.")
            break 

        else:
            turns -= 1   
                                        
            if turns == 0:
                print("you are not as smart as me, puny human.")
                print("Word was: "+ word_to_guess)
                break
main()
