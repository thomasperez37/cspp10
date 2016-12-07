import random
# function name: roll_dice
# purpose: rolls two random dice rolls,
# prints it out, and returns the sum
# arguments: None
# returns: the sum of the two dice
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("You rolled a {} and a {}. The total of your dice roll is {}.".format(dice1,dice2,dice_sum))
    return dice_sum

# function name: get_bet
# purpose: prints how much
# bank money you have,
# asks for how much you will
# bet, returns it and only
# accept valid bets
# arguments: bank_account
# returns: the bet money
def get_bet(bank_account):
    print("You have ${} in your bank account.".format(bank_account))
    bet_money = input("How much will you bet from your bank money for this round? ")
    while int(bet_money) > bank_account or int(bet_money) != float(bet_money) or int(bet_money) < 0:
        if int(bet_money) != float(bet_money) and int(bet_money) < 0:
            print("Your bet must be an integer and you can not bet negative money.")
            bet_money = input("I ask you again. How much will you bet for this round? ")
        elif int(bet_money) > bank_account and int(bet_money) != float(bet_money):
            print("Your bet must be an integer and you can not bet more than what you have in the bank.")
            bet_money = input("I ask you again. How much will you bet for this round? ")
        elif int(bet_money) > bank_account:
            print("Your bet money can not be more than what you have in the bank.")
            bet_money = input("I ask you again. How much will you bet for this round? ")
        elif int(bet_money) != float(bet_money):
            print("Your bet must be an integer.")
            bet_money = input("I ask you again. How much will you bet for this round? ")
        else:
            print("Your cannot bet negative money.")
            bet_money = input("I ask you again. How much will you bet for this round? ")