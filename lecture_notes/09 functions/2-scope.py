cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']

def f(s):

    a = len(s)

    return a

def f1():

    cities = ['Athens', 'Roma']

    def f(s):

        a = s.upper()

        return a

    print(cities)

    print(list(map(f, cities)))

    def f2():

        def f(s):

            a = s.lower()

            return a

        print(cities)

        print(list(map(f, cities)))

    def f3():

        cities = ['London', 'Beijing', 'Kiev']

        print(cities)

        print(list(map(f, cities)))

    f2()

    f3()




f1()

print(cities)

print(list(map(f, cities)))

