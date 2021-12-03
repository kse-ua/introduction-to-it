ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first = ages[0]
last = ages[-1]
ages.insert(5, 100)
ages.remove(18)
ages.pop()
ages.reverse()
print({'first': first, 'last': last})
print(ages)
