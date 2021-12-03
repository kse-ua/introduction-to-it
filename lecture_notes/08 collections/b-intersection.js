intersection = lambda set1, set2: set1 & set2

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}

print({
    'cities1': cities1,
    'cities2': cities2
})

results = intersection(cities1, cities2)
print(results)

