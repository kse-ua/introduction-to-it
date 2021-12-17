cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
cityLength = lambda s: [len(city) for city in s]


def f1():
    cities = ['Athens', 'Roma']
    cityUpper = lambda s: [city.upper() for city in s]

    print(cities)
    print(cityUpper(cities))

    cityLower = lambda s: [city.lower() for city in s]
    print(cities)
    print(cityLower(cities))

    cities = ['London', 'Beijing', 'Kiev']
    print(cities)
    print(cityUpper(cities))

f1()

print(cities)
print(cityLength(cities))
