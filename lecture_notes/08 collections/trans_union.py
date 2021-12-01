def union(set1, set2):
    unitedSet = set1
    for item in set2:
        if item not in set1:
            unitedSet.add(item)
    return unitedSet
    
cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}
print(f"cities1: {cities1}\n cities2: {cities2}")

results = union(cities1, cities2)
print(results)
