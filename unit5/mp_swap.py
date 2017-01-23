def swap(values,index1,index2):
    list_item1 = values[index1]
    list_item2 = values[index2]
    values[index1] = list_item2
    values[index2] = list_item1
a = [1,2,3,4,5,6,7]
swap(a,1,6)
print(a)