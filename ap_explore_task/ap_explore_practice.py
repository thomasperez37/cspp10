import random

def swap(values,index1,index2):
    list_item1 = values[index1]
    list_item2 = values[index2]
    values[index1] = list_item2
    values[index2] = list_item1

def seperator(word):
    letters = []
    for index in range(len(word)):
        letters.append(word[index])
    return letters
    
def scrambler(difficulty, word):
    for scramble_times in range(difficulty):
        index1 = random.randint(0,len(word)-1)