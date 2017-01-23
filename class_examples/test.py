num = " +5"
print(int(num))
def remove_all(original,target):
    counter = 0
    for index in range(len(original)):
        if original[index] == target:
            counter = counter + 1
    for remove_count in range(counter):
        original.remove(target)
a = [12,13,14,12,17,13,14,14,14,13,12]
remove_all(a,14)
print(a)