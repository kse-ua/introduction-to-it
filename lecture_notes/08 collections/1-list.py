ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

ages_set = set(ages)
ages = list(ages_set)
ages.insert(0, 8)
ages.append(22)

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })
