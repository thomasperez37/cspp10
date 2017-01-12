import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice1 = random.randint(1,6)
    # generate another random number from 1 to 6
    dice2 = random.randint(1,6)
    # get the sum of the two rolls
    dice_sum = dice1 + dice2
    # print the sum
    print("------------------------------")
    print("A {} and a {} were rolled. The total of your dice roll is {}.".format(dice1,dice2,dice_sum))
    # return the sum
    return dice_sum
    
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank_account):
    # ask the player how much they want to bet
    print("------------------------------")
    print("You have ${} in your bank account.".format(bank_account))
    bet_money = float(input("How much will you bet from your bank money for this round? "))
    # if player's bet is invalid,
    #   then get new bet
    while int(bet_money) > bank_account or int(bet_money) != bet_money or int(bet_money) < 0:
        if int(bet_money) != bet_money and int(bet_money) < 0:
            print("Your bet must be an integer and you can not bet nonexistent money.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        elif int(bet_money) > bank_account and int(bet_money) != bet_money:
            print("Your bet must be an integer and you can not bet more than what you have in the bank.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        elif int(bet_money) > bank_account:
            print("Your bet money can not be more than what you have in the bank.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        elif int(bet_money) != bet_money:
            print("Your bet must be an integer.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        else:
            print("Your cannot bet nonexistent money.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
    # if player's bet is valid, then return
    #   the bet
    return int(bet_money)
    
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over 7" if over 7
#           "under 7" if under 7
#           "equal 7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over 7"
    if dice_sum > 7:
        return "over 7"
    # if the sum is under 7, return "under 7"
    if dice_sum < 7:
        return "under 7"
    # if the sum is 7, return "equal 7"
    if dice_sum == 7:
        return "equal 7"
        
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over 7", "under 7", or "equal 7"
def choose_range():
    # present user with choices "over 7", "under 7",
    #   or "equal 7"
    print("Choose a range to roll for from the list below.")
    print("1. Roll for a number under 7.")
    print("2. Roll for a number over 7.")
    print("3. Roll for the number 7.")
    range_choice = input("Pick a range by typing it\'s corresponding number: ")
    # ask to choose range again if choice doesn't
    # correspond with anything
    while range_choice != '1' and range_choice != '2' and range_choice != '3':
        print("The only numbers are 1, 2, and 3.")
        range_choice = input("Just choose a range by typing it\'s corresponding number. ")
    # converts choice into recognizable words
    if range_choice == '1':
        range_choice = "under 7"
    elif range_choice == '2':
        range_choice = "over 7"
    else:
        range_choice = "equal 7"
    # return their choice
    return range_choice

# function to check if your roll won the bet
# name: check_roll
# arguments: the dice roll, it's outcome 
# and the range you chose for it
# returns: True or False
def check_roll(your_roll,outcome,chosen_range):
    # prints out outcome of the roll and returns
    # True, False, or "big win" based on the outcome
    if outcome == chosen_range:
        if outcome != "equal 7":
            print("You rolled a {} which is {} and that matches your range! Here\'s your bet money.".format(your_roll,outcome))
            return True
        else:
            print("You rolled a 7! You receive four times the amount of your bet!")
            return "big win"
    else:
        print("Sadly, that roll doesn\'t match your range. Give me your bet money.")
        return False
        
# function for the main game
# name: overunder7
# arguments: none
# returns: none
def overunder7():
    bank_money = 100
    while bank_money > 0:
        range_prompt = choose_range()