cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s: len(s)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s: s.upper()

    print(cities)
    print(list(map(f, cities)))

    def lowerPrint():
        f = lambda s: s.lower()
        print(cities)
        print(list(map(f, cities)))
    lowerPrint()

    def otherCities():
        cities = ['London', 'Beijing', 'Kiev']
        print(cities)
        print(list(map(f, cities)))
    otherCities()

f1()

print(cities)
print(list(map(f, cities)))


