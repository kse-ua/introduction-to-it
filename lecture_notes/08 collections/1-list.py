ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
print("Initial list:", ages)

ages.pop(0)
ages.append(25)
ages.extend([30])     # Additional method I found, so I've decided to demonstrate it

first = ages[0]
last = ages[-1]

print("Modified array list:", ages)
print({'first': first, 'last': last})
