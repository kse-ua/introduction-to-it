cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']


def f(cities):
    return [len(city) for city in cities]


def f1():
    cities = ['Athens', 'Roma']
    for city in range(len(cities)):
        cities[city] = cities[city].upper()
    return cities


def f2():
    cities = ['Athens', 'Roma']
    for city in range(len(cities)):
        cities[city] = cities[city].lower()
    return cities


print(f1())
print(f2())
print(cities)
print(f(cities))
