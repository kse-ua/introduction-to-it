difference = lambda set1, set2: set1.difference(set2)
complement = lambda set1, set2: difference(set2, set1)

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}

print({'cities1': cities1, 'cities2': cities2})

results = complement(cities1, cities2)
print(results)
