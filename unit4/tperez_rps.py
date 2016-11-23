import random
import getpass
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
#   purpose: present player with options, use getpass.getpass() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    p1_move = getpass.getpass("Player 1, choose your move only from [r, p, s]: ")
    while p1_move != 'r' and p1_move != 'p' and p1_move != 's':
        p1_move = getpass.getpass("Choose your move ONLY from [r, p, s]: ")
    return p1_move

#function name: get_p2_move():
#   arguments: none
#   purpose: present player with options, use getpass.getpass() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p2_move():
    p2_move = getpass.getpass("Player 2, choose your move only from [r, p, s]: ")
    while p2_move != 'r' and p2_move != 'p' and p2_move != 's':
        p2_move = getpass.getpass("Choose your move ONLY from [r, p, s]: ")
    return p2_move

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
#   purpose: based on the player 1 and player 2's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player1" if player1 won
#               "player2" if player2 won
#               "tie" if it's a tie
def get_round_winner(p1move, p2move):
    if p1move == "r" and p2move == "s":
        return "player1"
    elif p1move == "s" and p2move == "p":
        return "player1"
    elif p1move == "p" and p2move == "r":
        return "player1"
    elif p1move == "s" and p2move == "r":
        return "player2"
    elif p1move == "p" and p2move == "s":
        return "player2"
    elif p1move == "r" and p2move == "p":
        return "player2"
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
#   arguments: player 1 score, player 2 score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(p1score, p2score, ties):
    print("Player 1 Score: {}".format(p1score))
    print("Player 2 Score: {}".format(p2score))
    print("Ties: {}".format(ties))

def print_winner(p1score, p2score):
    if p1score > p2score:
        print("Based on the results, player 1 won the majority of the rounds! Congratulations Player 1!")
    elif p1score < p2score:
        print("Based on the results, player 2 won the majority of the rounds! Congratulations Player 2!")
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
    p1_score = 0
    p2_score = 0
    tie_score = 0
    rounds = get_rounds()
    round_number = 1
    score_objective = rounds//2 + 1
    while p1_score != score_objective and p2_score != score_objective and rounds != 0:
        print("------------------------------")
        print("Round {}!".format(round_number))
        p1_move = get_p1_move()
        p2_move = get_p2_move()
        full_p1_move = get_full_move(p1_move)
        full_p2_move = get_full_move(p2_move)
        print("Player 1's move: {}".format(full_p1_move))
        print("Player 2's move: {}".format(full_p2_move))
        if get_round_winner(p1_move, p2_move) == "player1":
            p1_score = p1_score + 1
            rounds = rounds - 1
            print("Player 1 won Round {}!".format(round_number))
            print_score(p1_score, p2_score, tie_score)
            round_number = round_number + 1
        elif get_round_winner(p1_move, p2_move) == "player2":
            p2_score = p2_score + 1
            rounds = rounds - 1
            print("Player 2 won Round {}!".format(round_number))
            print_score(p1_score, p2_score, tie_score)
            round_number = round_number + 1
        else:
            tie_score = tie_score + 1
            rounds = rounds - 1
            print("It was a tie for Round {}.".format(round_number))
            print_score(p1_score, p2_score, tie_score)
            score_objective = rounds//2 + 1
            round_number = round_number + 1
    print("------------------------------")
    print("Okay! Lets stop there. Here are the final scores.")
    print_score(p1_score, p2_score, tie_score)
    print_winner(p1_score, p2_score)
    print("GAME OVER")

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none

    

rps()