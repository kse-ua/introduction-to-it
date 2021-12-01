ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

ages.append(21)
print(ages)
ages.pop()
print(ages)
ages.insert(0, 9)
print(ages)
ages.remove(9)
print(ages)

print({ 'first': first, 'last': last })
