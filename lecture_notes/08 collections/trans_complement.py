cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}
print(f"cities1: {cities1}\n cities2: {cities2}")

results = cities1.difference(cities2)
print(results)
# alternative way 
print(cities1 - cities2)
