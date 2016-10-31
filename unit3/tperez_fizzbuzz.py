end_point = int(input("Input the end point of the Fizz Buzz sequence:"))
for num in range(1,end_point+1):
    len_of_num = len(str(num))
    for number in range(len_of_num):
        if (str(num)[number] == "3" or num % 3 == 0) and (str(num)[number] == "5" or num % 5 == 0):
            print("FizzBuzz,", end=" ")
            break
        elif str(num)[number] == "3" or num % 3 == 0:
            print("Fizz,", end=" ")
            break
        elif str(num)[number] == "5" or num % 5 == 0:
            print("Buzz,", end=" ")
            break
    else:
        print("{},".format(num), end=" ")