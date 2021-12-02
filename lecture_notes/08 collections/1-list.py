ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })

ages.append(-1003)
print(f"last : {ages[-1]}")

ages.pop()
print(f"last : {ages[-1]}")

ages.insert(0, -832)
print(f"first : {ages[0]}")

ages.pop(0)
print(f"first : {ages[0]}")

ages.sort()
print(ages)
