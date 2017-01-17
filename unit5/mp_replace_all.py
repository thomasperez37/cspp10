def replace_all(original,to_replace,replace_with):
    for index in range(len(original)):
        if original[index] == to_replace:
            original[index] = replace_with
a = [1,2,4,5,2,1,3,12,2]
replace_all(a,2,"win")
print(a)