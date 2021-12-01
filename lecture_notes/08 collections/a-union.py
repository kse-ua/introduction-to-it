cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']

first_cities = set(cities1)
second_cities = set(cities2)

dif = second_cities - first_cities

result = cities1 + list(dif)
print(result)
