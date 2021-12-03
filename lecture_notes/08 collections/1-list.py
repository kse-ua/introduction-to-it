ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })

ages.append(24)
pushed = ages[-1]

print({ 'pushed': pushed})

for x in range(2):
    ages.pop(-1)
popped = ages[-1]

print({ 'popped': popped})
