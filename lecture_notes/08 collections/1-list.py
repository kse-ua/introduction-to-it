ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })

ages.append(21) # Add at the end of list
print(ages)

ages.pop()
print(ages) # Remove  at the end of list

ages.insert(0,9) # Add at the top of list
print(ages)

ages.pop(0)
print(ages) # Remove at the top of list
