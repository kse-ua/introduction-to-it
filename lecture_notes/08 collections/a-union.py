def union_cities(s1, s2):
    difference = set(s2) - set(s1)
    result = s1 + list(difference)
    return result


cities1 = { 'Beijing', 'Kiev' }
cities2 = { 'Kiev', 'London', 'Baghdad' }

print(union_cities(cities1, cities2))
