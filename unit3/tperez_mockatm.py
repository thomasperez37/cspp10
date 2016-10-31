bank_account = 10000
print("Welcome to the ATM!")
options = input("Press 1 to withdraw, 2 to deposit and 3 to exit: ")
exit = 0
while exit == 0:
    if options == "1":
        withdraw = int(input("Input money to withdraw: "))
        while bank_account - withdraw < 0:
            print("Too much!")
            withdraw = int(input("Input money to withdraw: "))
        bank_account = bank_account - withdraw
        print("${}".format(bank_account))
        options = input("Press 1 to withdraw, 2 to deposit and 3 to exit: ")
    elif options == "2":
        deposit = int(input("Input money to deposit: "))
        bank_account = bank_account + deposit
        print("${}".format(bank_account))
        options = input("Press 1 to withdraw, 2 to deposit and 3 to exit: ")
    elif options == "3":
        exit = 1
    else:
        print("Not a valid input.")
        options = input("Press 1 to withdraw, 2 to deposit and 3 to exit: ")
print("Thanks for using the ATM!")