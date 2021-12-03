ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })

ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

print("Original list:", ages)

ages.append(123)
# add new element to the list
print(ages)

ages.remove(123)
# just delete written element
print(ages)

ages.pop(6)
# remove element by its index
print(ages)

ages.insert(6, 18)
# add element to list in oder to index
print(ages)

ages.reverse()
# reverse the order of the list
print(ages)
