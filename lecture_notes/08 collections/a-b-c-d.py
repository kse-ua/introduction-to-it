# Conditions
cities1 = set(['Beijing', 'Kiev'])
cities2 = set(['Kiev', 'London', 'Baghdad'])

# UNION-func
def union1(s1, s2):
    united_set = s1
    for item in s2:
        if item not in united_set:
            united_set.add(item)
    return united_set

print(union1(cities1, cities2))

# INTERSECTION-func
def intersection1(s1, s2):
    intersected_set = set()
    for item in s2:
        if item in s1:
            intersected_set.add(item)
    return intersected_set

print(intersection1(cities1, cities2))

# DIFFERENCE-func
def difference1(s1, s2):
    differenced_set = set()
    for item in s2:
        if item not in s1:
            differenced_set.add(item)
    for item in s1:
        if item not in s2:
            differenced_set.add(item)        
    return differenced_set

print(difference1(cities1, cities2))

# COMPLEMENT-func
def complement(s1, s2): 
    complemented_set = set() 
    for item in s1:
        if not item in s2:
            complemented_set.add(item)     
    return complemented_set

print(complement(cities1, cities2))

# UNION
results = cities1.union(cities2)
print(results)

# INTERSECTION
results = cities1.intersection(cities2)
print(results)

# DIFFERENCE
results = cities1.difference(cities2)
print(results)
