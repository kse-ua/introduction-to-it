def union(s_1, s_2):
    ds = set(s_1)
    for i in range (0, len(s_2)):
        item = s_2[i]
        if item not in ds:
            ds.add(item)
    return ds

def alt_union(s_1, s_2):
    ds = union(s_1, s_2)
    return ds

# Usage
cities_1 = ['Beijing', 'Kiev']
cities_2 = ['Kiev', 'London', 'Baghdad']
print(f"cities1: {cities_1}, cities2: {cities_2}")

results = union(cities_1, cities_2)
print(f"results: {results}")

alt_results = alt_union(cities_1, cities_2)
print(f"alternative results: {alt_results}")
