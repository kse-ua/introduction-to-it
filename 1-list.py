ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print(ages)

ages.append(575973650) 

print(ages)

print(f"{ages.pop()}, has been popped!")

print(ages)

ages.insert(0, 3124)

print(ages)

ages.pop(0)

print(ages)

print({'first': first, 'last': last})
