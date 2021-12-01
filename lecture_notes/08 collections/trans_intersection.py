def intersection(set1, set2):
    intersectedItems = set()
    for item in set1:
        if item in set2:
            intersectedItems.add(item)
    return intersectedItems

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}
print(f"cities1: {cities1}\n cities2: {cities2}")

results = intersection(cities1, cities2)
print(results)