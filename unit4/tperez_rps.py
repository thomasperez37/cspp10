import random
def ask_for_tutorial():
    tutorial_prompt = input("You do know how to play Rock, Paper, Scissors, right? Input [ y or n ]: ")
    while tutorial_prompt != 'y' and tutorial_prompt != 'n':
        tutorial_prompt = input("\'y\' is for YES and \'n\' is for NO [ y or n ]: ")
    return tutorial_prompt
        
def give_tutorial():
    print("------------------------------")
    print("Wow...")
    print("Uh...well anyway, you and the computer will choose Rock, Paper, or Scissors. Each item is strong against one item and weak against another.")
    print("Rock is strong against Scissors and weak against Paper.")
    print("Paper is strong against Rock and weak against Scissors.")
    print("Scissors is strong against Paper and weak against Rock.")
    print("If you pick a stronger item, you win a round.")
    print("If you pick a weaker item, you lose a round.")
    print("If you choose the same item as the computer, it's a tie.")
    print("After all the rounds, I'll give you the scoreboard and tell you who won.")
#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    your_move = input("Choose your move only from [r, p, s]: ")
    while your_move != 'r' and your_move != 'p' and your_move != 's':
        your_move = input("Choose your move ONLY from [r, p, s]: ")
    return your_move

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    return "rps"[random.randint(0,2)]

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    print("------------------------------")
    print("Caution: We need you to input the number of rounds for the game but if you input a letter, an error will occur.")
    num_of_rounds = input("Choose the number of rounds only from [1 to 9]: ")
    while int(num_of_rounds) < 1 or int(num_of_rounds) > 9:
        num_of_rounds = input("Choose the number of rounds ONLY from [1 to 9]: ")
    return int(num_of_rounds)
   

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    if p1move == "r" and cmove == "s":
        return "player"
    elif p1move == "s" and cmove == "p":
        return "player"
    elif p1move == "p" and cmove == "r":
        return "player"
    elif p1move == "s" and cmove == "r":
        return "comp"
    elif p1move == "p" and cmove == "s":
        return "comp"
    elif p1move == "r" and cmove == "p":
        return "comp"
    else:
        return "tie"
#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    if shortmove == 'r':
        return 'Rock'
    elif shortmove == 's':
        return 'Scissors'
    else:
        return 'Paper'

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    print("Player Score: {}".format(pscore))
    print("Computer Score: {}".format(cscore))
    print("Ties: {}".format(ties))

def print_winner(pscore, cscore):
    if pscore > cscore:
        print("Based on the results, you won the majority of the rounds! Congratulations!")
    elif pscore < cscore:
        print("Based on the results, the computer won the majority of the rounds. Better luck next time.")
    else:
        print("Based on the results, no one wins. It's a tie.")
#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    print("Let's play Rock, Paper, Scissors!")
    if ask_for_tutorial() == 'n':
        give_tutorial()
    print("Well then, let\'s begin.")
    p_score = 0
    c_score = 0
    tie_score = 0
    rounds = get_rounds()
    round_number = 1
    score_objective = rounds//2 + 1
    while p_score != (score_objective-tie_score) and c_score != (score_objective-tie_score) and rounds != 0:
        print("------------------------------")
        print("Round {}!".format(round_number))
        p_move = get_p1_move()
        c_move = get_comp_move()
        full_p_move = get_full_move(p_move)
        full_c_move = get_full_move(c_move)
        print("Your move: {}".format(full_p_move))
        print("Computer's move: {}".format(full_c_move))
        if get_round_winner(p_move, c_move) == "player":
            p_score = p_score + 1
            rounds = rounds - 1
            print("You won Round {}!".format(round_number))
            print_score(p_score, c_score, tie_score)
            round_number = round_number + 1
        elif get_round_winner(p_move, c_move) == "comp":
            c_score = c_score + 1
            rounds = rounds - 1
            print("The computer won Round {}...".format(round_number))
            print_score(p_score, c_score, tie_score)
            round_number = round_number + 1
        else:
            tie_score = tie_score + 1
            rounds = rounds - 1
            print("You got a tie for Round {}".format(round_number))
            print_score(p_score, c_score, tie_score)
            round_number = round_number + 1
    print("------------------------------")
    print("Okay! Lets stop there. Here are the final scores.")
    print_score(p_score, c_score, tie_score)
    print_winner(p_score, c_score)
    print("GAME OVER")

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none

    

rps()