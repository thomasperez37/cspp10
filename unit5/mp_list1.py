num_list = []
num_input = int(input("Enter a positive number to add it to the list and enter a zero to exit this app: "))
while num_input != 0:
    if num_input < 0 and -num_input in num_list:
        num_list.remove(-num_input)
        print(num_list)
        num_input = int(input("Enter a positive number to add it to the list, enter a negative number to remove it\'s positive counterpart and enter a zero to exit this app: "))
    elif num_input < 0:
        print(num_list)
        print("{} doesn't exist in the list.".format(-num_input))
        num_input = int(input("Enter a positive number to add it to the list, enter a negative number to remove it\'s positive counterpart and enter a zero to exit this app: "))
    else:
        num_list.append(num_input)
        print(num_list)
        num_input = int(input("Enter a positive number to add it to the list, enter a negative number to remove it\'s positive counterpart and enter a zero to exit this app: "))
print("PROGRAM END")