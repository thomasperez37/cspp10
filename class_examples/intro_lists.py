names = []
run_loop = True
while run_loop:
    name_choice = input("Enter a name: ")
    names.insert(0,name_choice)
    print(names)
    if names[0] == "done":
        run_loop = False