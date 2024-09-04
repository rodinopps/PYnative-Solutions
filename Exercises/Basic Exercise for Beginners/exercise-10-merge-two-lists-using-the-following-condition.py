list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

newlist = []
for i in range(len(list1)):
    if list1[i] % 2 == 1:
        newlist.append(list1[i])
    if list2[i] % 2 == 0:
        newlist.append(list2[i])
newlist.sort()

print(newlist)
