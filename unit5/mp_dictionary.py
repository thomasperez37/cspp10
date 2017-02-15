from pprint import pprint

def add(dictionary_list):
    new_key = input()
    new_value = input()
    while new_key in dictionary_list:
        new_key = input()
        new_value = input()
    dictionary_list[new_key] = new_value
    
def remove_key(dictionary_list):
    selected_key = input()
    if selected_key in dictionary_list:
        del dictionary_list[selected_key]
    
def remove_value(dictionary_list):
    selected_value = input()
    for key in dictionary_list:
        if dictionary_list[key] == selected_value:
            del dictionary_list[key]
    
def update(dictionary_list):
    selected_key = input()
    if selected_key in dictionary_list:
        selected_value = input()
        dictionary_list[selected_key] = selected_value
        
def give_dictionary_options():
    dictionary = {}
    selected_option = input()