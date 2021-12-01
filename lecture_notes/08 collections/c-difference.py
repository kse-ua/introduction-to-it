def intersection(s1, s2):
    return set(s1) - set(s2)


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']

print(intersection(cities1, cities2))
