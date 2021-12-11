cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
def f(s):
    return len(s)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s: s.upper()

    print(cities)
    print(list(map(f, cities)))

    def lowerCities():
        f = lambda s: s.lower()
        print(cities)
        print(list(map(f, cities)))
    lowerCities()

    def upperCities():
        cities = ['London', 'Beijing', 'Kiev']
        print(cities)
        print(list(map(f, cities)))
    upperCities()

f1()

print(cities)
print(list(map(f, cities)))
