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
# to perform the code, i'll simply print the second function
# challenge notes: in order to shuffle a word without shuffle()
# then i need to use random.randint() to pick random indexes according to 
# the length of the word list
# I would use these indexes in swap() and I would assemble the new word
# the same way as usual

import random
from mp_swap import swap

def scramble_word(word_item):
    if len(word_item) > 3:
        all_letters = list(word_item)
        first_letter = all_letters[:1]
        last_letter = all_letters[-1:]
        remaining_letters = all_letters[1:len(all_letters)-1]
        remaining_letters_copy1 = ''.join(remaining_letters)
        remaining_letters_copy2 = ''.join(remaining_letters)
        #I just noticed that if all the letters in remaining_letters are
        #all the same, the middle part of the word could never change
        #therefore, i will simply return the word unscrambled in
        #such cases
        if all(x == remaining_letters[0] for x in remaining_letters):
            return word_item
        while remaining_letters_copy1 == remaining_letters_copy2:
            for scramble_times in range(5):
                index1 = random.randint(0,len(remaining_letters)-1)
                index2 = random.randint(0,len(remaining_letters)-1)
                while index1 == index2:
                    index1 = random.randint(0,len(remaining_letters)-1)
                    index2 = random.randint(0,len(remaining_letters)-1)
                swap(remaining_letters,index1,index2)
            remaining_letters_copy2 = ''.join(remaining_letters)
        new_letters = first_letter + remaining_letters + last_letter
        new_word = ''.join(new_letters)
        return new_word
    return word_item
    
def scramble_phase(phrase):
    word_list = phrase.split(" ")
    for index in range(len(word_list)):
        word_list[index] = scramble_word(word_list[index])
    new_phrase = " ".join(word_list)
    return new_phrase
    
print(scramble_phase(input("Please enter the phrase you want scrambled: ")))