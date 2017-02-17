# import random https://docs.google.com/document/d/1O8tJ3CZ7pSJCjCd1kCQ-ekdmxZI-6csQ7jzU1AwIi2A/edit
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
from mp_swap import swap

def scramble_word(word_item):
    if len(word_item) > 3:
        all_letters = list(word_item)
        first_letter = all_letters[:1]
        last_letter = all_letters[-1:]
        remaining_letters = all_letters[1:len(all_letters)-1]#edit this mores
        remaining_letters_copy1 = ''.join(remaining_letters)#edit this more
        remaining_letters_copy2 = ''.join(remaining_letters)
        while remaining_letters_copy1 == remaining_letters_copy2:
            for scramble_times in range(5):
                index1 = random.randint(0,len(remaining_letters)-1)
                index2 = random.randint(0,len(remaining_letters)-1)
                while index1 == index2:
                    index1 = random.randint(0,len(remaining_letters)-1)
                    index2 = random.randint(0,len(remaining_letters)-1)
                swap(remaining_letters,index1,index2)
            remaining_letters_copy2 = ''.join(remaining_letters)
        new_letters = remaining_letters
        new_letters.insert(0,first_letter)
        new_letters.append(last_letter)
        new_word = ''.join(new_letters)
        return new_word
    return word_item
    
def scramble_phase(phrase):
    word_list = phrase.split(" ")
    for word in word_list:
        word = scramble_word(word)
    new_phrase = " ".join(word_list)
    return new_phrase
    
scramble_phase(input("Please enter the phrase you want scrambled: "))