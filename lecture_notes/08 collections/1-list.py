ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

# del last elem fron the list
ages.pop()

# add elem at the beggining of the list
ages.insert(0, 9)

# del first elem
del ages[0]

# add elem at the end
ages.append(21)

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })
