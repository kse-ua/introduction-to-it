ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ first, last })

# list methods
ages.append(25)
ages.pop(-1)
# list return to the original form
# add to the top of list
ages.insert(0, 25)
ages.pop(0)
# list return to the original form
# del method
del ages[-1]
print(ages)

names = ['Timur', 'Anna', 'Dmytro', 'Veronika']
# alphabetical order ['Anna', 'Dmytro', 'Timur', 'Veronika'], not permanent change
sorted_list = sorted(names)
# reverse order ['Veronika', 'Timur', 'Dmytro', 'Anna']
sorted_list.reverse()
# alphabetical order ['Anna', 'Dmytro', 'Timur', 'Veronika'], permanent change
names.sort()
# permanent reverse
names.sort(reverse=True)
print(names)
