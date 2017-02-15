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
        
def ask_for_scramble_difficulty():
    print("---------------------------------------------------------")
    print("Scramble Difficulty:")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    scramble_difficulty = input("Pick the corresponding number to your choice of difficulty for how much you want the words to be scrambled: ")
    while scramble_difficulty != '1' and scramble_difficulty != '2' and scramble_difficulty != '3':
        scramble_difficulty = input("Just type \'1,\' \'2,\' or \'3\': ")
    return int(scramble_difficulty)
    
def ask_for_tutorial():
    print("---------------------------------------------------------")
    tutorial_prompt = input("Do you know how to play Scrambled Sorting?[\'y\' or \'n\'] ")
    while tutorial_prompt != 'y' and tutorial_prompt != 'n':
        tutorial_prompt = input("Yes is \'y\' and no is \'n\'. So I\'ll ask you again. Do you know how to play Scrambled Sorting? ")
    return tutorial_prompt
    
def give_tutorial():
    print("---------------------------------------------------------")
    print("Basic Info:")
    print("In Scrambled Sorting, you will go through rounds to earn points where the difficulty of the game determines how many points you")
    print("gain each round. In order to win points, you give the computer a certain number of words and the computer will scramble all them")
    input("Press enter to continue")
    print("")
    print("Regarding the Setup Process:")
    print("In the beginning, we\'ll ask you")

def ask_to_end_game():
    quit_prompt = input("Do you want to keep going?[\'y\' or \'n\'] ")
    while quit_prompt != 'y' and quit_prompt != 'n':
        quit_prompt = input("Yes is \'y\' and no is \'n\'. So I\'ll ask you again. Do you want to keep going? ")
    if quit_prompt == 'n':
        return False
    return True
        
def print_info(score,lives):
    print("Score:{}".format(score))
    print("Remaining Lives:{}")

def scrambled_sorting():
    print("Welcome to Scrambled Sorting!")
    input("Press enter to play")
    tutorial_answer = ask_for_tutorial()
    if tutorial_answer == 'y':
        give_tutorial()
    print("Okay then! Lets begin!")
    difficulty = ask_for_scramble_difficulty()
    word_amount = int(input("Now, how many words do you want to work with for each round? "))
    points = 0
    lives = 4 - difficulty
    round_counter = 1
    run_game = True
    print("Here is your score and lives.")
    print_info(points,lives)
    print("Okay, are you ready to play?")
    input("Press enter to start round 1")
    while run_game:
        print("Round {}!".format(round_counter))
        