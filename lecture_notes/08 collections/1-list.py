ages = [10, 12, 15, 15, 17, 18, 18, 19]

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })

ages.append(29) # Add at the end of array
print(ages)

ages.pop() # remove at the end of array
print(ages)

ages.insert(0,5) # Add at the top of array
print(ages)

ages.pop(-1) # remove at the top of array
print(ages)
