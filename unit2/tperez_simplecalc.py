equation = input("Input equation with no spaces: ")
lenfirstterm = int(input("What is the length of the first term? "))
lensecondterm = int(input("What is the length of the second term? "))
firstterm = int(equation[:lenfirstterm])
mathsign = equation[lenfirstterm]
secondterm = int(equation[-lensecondterm:])
if mathsign == '+':
    equalto = firstterm+secondterm
    print("The result is {}.".format(equalto))
elif mathsign == '-':
    equalto = firstterm-secondterm
    print("The result is {}.".format(equalto))
elif mathsign == '*':
    equalto = firstterm*secondterm
    print("The result is {}.".format(equalto))
elif mathsign == '/':
    equalto = firstterm/secondterm
    print("The result is {}.".format(equalto))
elif mathsign == '%':
    equalto = firstterm%secondterm
    print("The result is {}.".format(equalto))
else:
    print("Error!")