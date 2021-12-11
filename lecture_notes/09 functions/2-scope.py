cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s: len(s)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s: s.upper()

    print(cities)
    print(list(map(f, cities)))

    def f2():
        f = lambda s: s.lower()
        print(cities)
        print(list(map(f, cities)))
    f2()

    def f3():
        cities = ['London', 'Beijing', 'Kiev']
        print(cities)
        print(list(map(f, cities)))
    f3()

f1()

print(cities)
print(list(map(f, cities)))
