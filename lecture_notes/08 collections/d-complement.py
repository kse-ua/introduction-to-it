difference = lambda s1, s2: s1.difference(s2)
complement = lambda s1, s2: difference(s2, s1)

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}

print({'cities1': cities1, 'cities2': cities2})

results = complement(cities1, cities2)
print(results)
