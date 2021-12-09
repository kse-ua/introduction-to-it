cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
def f(s): return len(s)


def f1():
    cities = ['Athens', 'Roma']
    def f(s): return s.upper()

    print(cities)
    print(list(map(f, cities)))

    def f2():
        def f(s): return s.lower()
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
