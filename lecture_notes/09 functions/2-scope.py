cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
def f(s):
    return len(s)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s: s.upper()

    print(cities)
    print(list(map(f, cities)))

    f = lambda s: s.lower()
    print(cities)
    print(list(map(f, cities)))

    f = lambda s: s.upper()
    cities = ['London', 'Beijing', 'Kiev']
    print(cities)
    print(list(map(f, cities)))
    

f1()
length = f(cities)
print(f" cities: {cities}")
print(list(map(f, cities)))
