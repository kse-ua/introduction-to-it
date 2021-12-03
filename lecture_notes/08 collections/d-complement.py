def difference(s_1, s_2):
    ds = set()
    for i in range (0, len(s_1)):
        item = s_1[i]
        if item not in s_2:
            ds.add(item)
    return ds

def alt_difference(s_1, s_2):
    ds = difference(s_1, s_2)
    return ds

def complement(s_1, s_2):
    ds = difference(s_2, s_1)
    return ds

# Usage
cities_1 = ['Beijing', 'Kiev']
cities_2 = ['Kiev', 'London', 'Baghdad']
print(f"cities1: {cities_1}, cities2: {cities_2}")

results = complement(cities_1, cities_2)
print(f"results: {results}")
