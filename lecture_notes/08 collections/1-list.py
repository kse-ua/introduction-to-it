ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

ages.append(30)
ages.remove(15)
ages.pop()
del ages[2]

print({ 'first': first, 'last': last })
