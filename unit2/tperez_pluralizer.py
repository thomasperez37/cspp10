amount = int(input("Input the amount of the noun: "))
noun = input("Input the singular noun: ")
if amount == 1:
    print("1 {}".format(noun))
elif amount > 1 and noun == "child":
    print("{} children".format(amount))
elif amount > 1 and noun[-2:] == "an":
    print("{} {}en".format(amount,noun[:-2]))
elif amount > 1 and noun == "person":
    print("{} people".format(amount))
elif amount > 1 and noun == "goose":
    print("{} geese".format(amount))
elif amount > 1 and noun == "mouse":
    print("{} mice".format(amount))
elif amount > 1 and (noun == "deer" or noun == "sheep" or noun == "aircraft" or noun == "fish" or noun == "species"):
    print("{} {}".format(amount,noun))
elif amount > 1 and (noun == "dwarf" or noun == "roof"):
    print("{} {}s".format(amount,noun))
elif amount > 1 and noun == "foot":
    print("{} feet".format(amount))
elif amount > 1 and noun == "tooth":
    print("{} teeth".format(amount))
elif amount > 1 and noun == "datum":
    print("{} data".format(amount))
elif amount > 1 and (noun == "news" or noun == "athletics" or noun == "linguistics" or noun == "darts" or noun == "billiards"):
    print("{} {}".format(amount,noun))
