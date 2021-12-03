union = lambda s1, s2: s1 | s2

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}

print({f"cities1": cities1})
print({f"cities2": cities2})

results = union(cities1, cities2)

print(results)
