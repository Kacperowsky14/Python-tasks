list1 = [1,2,4,0,6,67,4,3,2,5,7,8,3]
list2 = [5,2,3,5,8,3,3,5,7,9,0,]
list3 = []

for i in list1:
    if i in list2:
        list3.append(i)
print(list3)
