cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda x: len(cities)


def f1():
    cities = ['Athens', 'Roma']
    print('cities:', cities)
    cities_upper = list(map(str.upper, cities))  # list(map(lambda x: x.upper()
    print(cities_upper)

    def f2():
        print('cities:', cities)
        cities_lower = list(map(str.lower, cities))
        print(cities_lower)
    f2()

    def f3():
        cities = ['London', 'Beijing', 'Kiev']
        print('cities:', cities)
        cities_upper = list(map(str.upper, cities))
        print(cities_upper)
    f3()


f1()
print('cities:', cities)
print(list(map(f, cities)))
