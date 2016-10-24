#Note: I used two websites that explained plural noun rules very well so I have rules for plural nouns but not every special noun may be included.
amount = int(input("Input the amount of the noun: "))
noun = input("Input the singular noun: ")
#This if statement will determine if the noun is singular
if amount == 1:
    print("1 {}".format(noun))
#These longer elif statements are meant to catch a specific group of special words that I couldn't group with a single print statement.
elif amount != 1 and (noun == "trousers" or noun=="jeans" or noun == "glasses" or noun == "savings" or noun == "thanks" or noun == "steps" or noun == "stairs" or noun == "customs" or noun == "congratulations" or noun == "tropics" or noun == "wages" or noun == "spectacles" or noun == "outskirts" or noun == "goods" or noun == "wits" or noun == "news" or noun == "athletics" or noun == "linguistics" or noun == "billiards"):
    print("{} {}".format(amount,noun))
elif amount != 1 and (noun == "deer" or noun == "sheep" or noun == "aircraft" or noun == "fish" or noun == "species"):
    print("{} {}".format(amount,noun))
elif amount != 1 and (noun == "dwarf" or noun == "roof" or noun == "turf"):
    print("{} {}s".format(amount,noun))
elif amount != 1 and (noun == "criterion" or noun == "phenomenon"):
    print("{} {}a".format(amount,noun[:-2])) 
elif amount != 1 and (noun == "man" or noun == "woman"):
    print("{} {}en".format(amount,noun[:-2]))
#These short elif statements are for pluralizing some special words that can't be grouped in to many things.
elif amount != 1 and noun == "child":
    print("{} children".format(amount))
elif amount != 1 and noun == "person":
    print("{} people".format(amount))
elif amount != 1 and noun == "cafe":
    print("{} cafes".format(amount))
elif amount != 1 and noun == "goose":
    print("{} geese".format(amount))
elif amount != 1 and noun == "mouse":
    print("{} mice".format(amount))
elif amount != 1 and noun == "beef":
    print("{} beefs".format(amount))
elif amount != 1 and noun == "foot":
    print("{} feet".format(amount))
elif amount != 1 and noun == "tooth":
    print("{} teeth".format(amount))
elif amount != 1 and noun == "datum":
    print("{} data".format(amount))
elif amount != 1 and noun == "bus":
    print("{} buses".format(amount))
#These set of elif statements group non-specific singular nouns into general rules and pluralizes them.
elif amount != 1 and noun[-2:] == "is":
    print("{} {}es".format(amount,noun[:-2]))
elif amount != 1 and noun[-2:] == "us":
    print("{} {}i".format(amount,noun[:-2]))
elif amount != 1 and noun[-1:] == "o":
    print("{} {}es".format(amount,noun))
elif amount != 1 and noun[-2:] == "fe":
    print("{} {}ves".format(amount, noun[:-2]))
elif amount != 1 and noun[-1:] == "f":
    print("{} {}ves".format(amount,noun[:-1]))
elif amount != 1 and (noun[-1:] == "s" or noun[-1:] == "x" or noun[-1:] == "z"):
    print("{} {}es".format(amount,noun))
elif amount != 1 and (noun[-2:] == "ch" or noun[-2:] == "sh"):
    print("{} {}es".format(amount,noun))
elif amount != 1 and (noun[-2:] == "oy" or noun[-2:] == 'ay' or noun[-2:] == 'ey' or noun[-2:] == 'uy'):
    print("{} {}s".format(amount,noun))
elif amount != 1 and noun[-1:] == 'y':
    print("{} {}ies".format(amount,noun[:-1]))
else:
    print("{} {}s".format(amount,noun))
