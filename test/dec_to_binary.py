print("Decimator to Binary Translator!")
input("Press enter to continue.")
print("")
amount_of_bits = int(input("How many bits do you want to use? Type in a whole number: "))
dec_range = 0
bits = []
multi_of_two = []
# 32 16 8 4 2 1 if dec_num is less than first number, check against next number     this comment is a reminder for myself
for digit in range(amount_of_bits):
    range_increase = 2**digit
    dec_range = dec_range + range_increase
    multi_of_two.append(range_increase)
multi_of_two.reverse()
print("")
dec_num = int(input("What decimal number do you want translated? Type in a whole number: "))
while dec_num < 0 or dec_num > dec_range:
    print("")
    print("Error")
    print("")
    dec_num = int(input("What decimal number do you want translated? Type in a whole number: "))
if dec_num == 0:
    print("")
    for num in range(amount_of_bits):
        print("0", end="")
else:
    print("")
    for n in multi_of_two:
        if n > dec_num:
            bits.append("0")
        else:
            dec_num = dec_num - n
            bits.append("1")
    for bit in bits:
        print("{}".format(bit), end="")
    