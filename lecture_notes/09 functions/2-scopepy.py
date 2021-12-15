cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']


def c1(cities):
    return [len(city) for city in cities]

def c2():
    cities = ['Athens', 'Roma']
    for city in range(len(cities)):
        cities[city] = cities[city].upper()
    return cities

def c3():
    cities = ['Athens', 'Roma']
    for city in range(len(cities)):
        cities[city] = cities[city].lower()
    return cities

print(c2())
print(c3())
print(cities)
print(c1(cities))
