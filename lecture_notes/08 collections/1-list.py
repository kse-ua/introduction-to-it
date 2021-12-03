ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]
ages.pop()
ages.insert(0, 9)
del ages[0]
ages.append(21)

print({'first': first, 'last': last})
