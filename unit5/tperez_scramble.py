# import random
# define a function that only scrambles 4 letter long words,
# turns the strings into lists, does not shuffle the first and last letter,
# and returns the scrambled word
# maybe I could assign 1st and last to variables
# extra note: if I use while loops, I can rescramble words
# if they stay the same
# then i'll define a function that makes a list of words to be scrambled
# through string.split()
# then i'll use a for loop to
# go through each word and scramble each word using the first function
# to perform the code, i'll simply call the second function
# challenge notes: in order to shuffle a word without shuffle()
# then i need to use random.randint() to pick random indexes according to 
# the length of the word list
# I would use these indexes in swap() and I would assemble the new word
# the same way as usual

import random

def scramble_word(word_item):
    if len(word_item) > 3:
        letters = list(word_item)
        first_letter = letters[:1]
        second_letter = letters[-1:]