equation = input("Input equation with no spaces: ")
#In order to retrieve the terms from this equation, I need the length of them.
len_first_term = int(input("What is the length of the first term? "))
len_second_term = int(input("What is the length of the second term? "))
#Now I can pick out the terms and their math sign.
first_term = int(equation[:len_first_term])
math_sign = equation[len_first_term]
second_term = int(equation[-len_second_term:])
#These if and elif statements will determine the equation we have. Then, it will print out what it is equal to.
if math_sign == '+':
    print("The result is {}.".format(first_term + second_term))
elif math_sign == '-':
    print("The result is {}.".format(first_term - second_term))
elif math_sign == '*':
    print("The result is {}.".format(first_term * second_term))
elif math_sign == '/':
    print("The result is {}.".format(first_term / second_term))
elif math_sign == '%':
    print("The result is {}.".format(first_term % second_term))
else:
    print("Error!")