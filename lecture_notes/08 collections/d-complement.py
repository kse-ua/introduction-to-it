def complement(s1, s2, list3):

    for i in s2:
        if i not in s1:
            list3.append(i)
    return list3


list1 = ['Beijing', 'Kiev']
list2 = ['Kiev', 'London', 'Baghdad']

complementList = []

print(complement(list1, list2, complementList))
