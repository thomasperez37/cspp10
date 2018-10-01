def extend(original,extension):
    for element in extension:
        original.append(element)
a = [1,2,3]
b = [4,5,6]
extend(a,b)
print(a)
print(b)