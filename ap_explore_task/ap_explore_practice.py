import random

def swap(values,index1,index2):
    list_item1 = values[index1]
    list_item2 = values[index2]
    values[index1] = list_item2
    values[index2] = list_item1
    
def scramble_to_difficulty(difficulty, word):
    letters = list(word)
    for scramble_times in range(difficulty):
        index1 = random.randint(0,len(word)-1)
        index2 = random.randint(0,len(word)-1)
        while index1 == index2:
            index1 = random.randint(0,len(word)-1)
            index2 = random.randint(0,len(word)-1)
        swap(letters,index1,index2)
    new_word = ''.join(letters)
    while new_word == word:
        letters = list(word)
        for scramble_times in range(difficulty):
            index1 = random.randint(0,len(word)-1)
            index2 = random.randint(0,len(word)-1)
            while index1 == index2:
                index1 = random.randint(0,len(word)-1)
                index2 = random.randint(0,len(word)-1)
            swap(letters,index1,index2)
        new_word = ''.join(letters)
    return new_word
        