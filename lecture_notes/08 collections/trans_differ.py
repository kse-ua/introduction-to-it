def difference(set1, set2):
    difference = set()
    for item in set1:
        if item not in set2:
            difference.add(item)
    for item in set2:
        if item not in set1:
            difference.add(item)
    return difference

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}
print(f"cities1: {cities1}\n cities2: {cities2}")

results = difference(cities1, cities2)
print(results)

# alternative way 
print(cities2 ^ cities1)
