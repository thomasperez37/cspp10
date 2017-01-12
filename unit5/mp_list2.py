num_list = []
print("You can type a number to add it to a list, type the word \"sum\" to add the listed numbers together and show it to you, type the word \"clear\" to clear all listed numbers, type the word \"print\" to show the list, type the word \"length\" to show you")
print("the length of the list, and type the word \"exit\" to end the program.")
choice_of_input = input("Enter a number or a command: ")
while choice_of_input != "exit":
    num_checker = 0
    string_checker = False
    for index in range(len(choice_of_input)):
        if choice_of_input[index] == "0" or choice_of_input[index] == "1" or choice_of_input[index] == "2" or choice_of_input[index] == "3" or choice_of_input[index] == "4" or choice_of_input[index] == "5" or choice_of_input[index] == "6" or choice_of_input[index] == "7" or choice_of_input[index] == "8" or choice_of_input[index] == "9":
            num_checker = num_checker + 1
        elif choice_of_input[index] == "+" or choice_of_input[index] == "-" or choice_of_input == " ":
            num_checker = num_checker + 0
        else:
            string_checker = True
    if num_checker > 0 and string_checker == False:      
        num_list.append(int(choice_of_input))
        choice_of_input = input("Enter a number or a command: ")
    if choice_of_input == "sum":
        accumulator = 0
        for num in range(len(num_list)):
            accumulator = accumulator + num_list[num]
        print("The sum of all the numbers in the list is {}.".format(accumulator))
        choice_of_input = input("Enter a number or a command: ")
    elif choice_of_input == "clear":
        for num in range(len(num_list)):
            num_list.remove(num_list[num])
        choice_of_input = input("Enter a number or a command: ")
    elif choice_of_input == "print":
        print(num_list)
        choice_of_input = input("Enter a number or a command: ")
    elif choice_of_input == "length":
        print("The length of the list is {}.".format(len(num_list)))
        choice_of_input = input("Enter a number or a command: ") 
    else:
        print("Not a valid input.")
        choice_of_input = input("Enter a number or a command: ") 
print("PROGRAM END")        