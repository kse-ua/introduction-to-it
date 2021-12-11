difference = lambda a, b: a - b
complement = lambda a, b: difference(a, b)

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}

result = complement(cities2, cities1)
print(result)
