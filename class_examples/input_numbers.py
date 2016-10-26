final = ""
inp = input("Enter a number or exit: ")
while inp != "exit":
    final = final + inp + " "
    inp = input("Enter a number or exit: ")
print(final)