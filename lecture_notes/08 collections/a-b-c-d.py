# Usage
# Conditions
cities1 = set(['Beijing', 'Kiev'])
cities2 = set(['Kiev', 'London', 'Baghdad'])

# UNION
results = cities1.union(cities2)
print(results)

# INTERSECTION
results = cities1.intersection(cities2)
print(results)

# DIFFERENCE
results = cities1.difference(cities2)
print(results)

# COMPLEMENT
results = cities1.union(cities2) - cities1
print(results)
