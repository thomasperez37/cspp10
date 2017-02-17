from pprint import pprint

def add(dictionary_list):
    new_key = input("Type in a word for the key of the new key-value pair: ")
    new_value = input("Type in a word for the value of the new key-value pair: ")
    while new_key in dictionary_list:
        print("That key already exists!")
        new_key = input("Type in a different word for the key of the new key-value pair: ")
        new_value = input("Type in a word for the value of the new key-value pair: ")
    dictionary_list[new_key] = new_value
    
def remove_key(dictionary_list):
    selected_key = input("Type in the word of the key of the key-value pair you want to remove: ")
    if selected_key in dictionary_list:
        del dictionary_list[selected_key]
    
def update(dictionary_list):
    selected_key = input("Type in the word of the key of the key-value pair you want to change: ")
    if selected_key in dictionary_list:
        new_value = input("Type in a word for the new value of the key-value pair: ")
        dictionary_list[selected_key] = new_value

def give_dictionary_options():
    dictionary = {}
    print("You have 5 options. Type in \'add\' to be able to add a new key-value pair. However, you won\'t be able to add a new key-value pair that has the same key as another pair.")
    print("Type in \'remove_key\' to be able to remove a key-value pair by typing it\'s corresponding key.")
    print("Type in \'update\' to be able to change an already existing key-value pair\'s value.")
    print("Type in \'print\' to print out the dictionary.")
    print("Type in \'exit\' to end the program.")
    selected_option = input("Please choose one of the 5 options: ")
    while selected_option != 'exit':
        if selected_option == 'add':
            add(dictionary)
            selected_option = input("Please choose another one of the 5 options: ")
        elif selected_option == 'remove_key':
            remove_key(dictionary)
            selected_option = input("Please choose another one of the 5 options: ")
        elif selected_option == 'update':
            update(dictionary)
            selected_option = input("Please choose another one of the 5 options: ")
        elif selected_option == 'print':
            pprint(dictionary)
            selected_option = input("Please choose another one of the 5 options: ")
        else:
            print("Not a valid option")
            selected_option = input("Please choose another one of the 5 options: ")
    print("PROGRAM END")
            
give_dictionary_options()