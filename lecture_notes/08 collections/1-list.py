ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })

ages.insert(0, 6)
shifted = ages[0]

print({ 'shifted': shifted })

for x in range(2):
    ages.pop(0)
unshifted = ages[0]

print({ 'unshifted': unshifted})
