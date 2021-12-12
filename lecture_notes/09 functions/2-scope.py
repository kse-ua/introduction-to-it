cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
def f(s):
    len_s = len(s)
    return len_s


def f1():
    cities = ['Athens', 'Roma']
    def f(s):
        ns = s.upper()
        return ns
    print(cities)
    print(list(map(f, cities)), '\n')

    def f2():
        def f(s):
            ns = s.lower()
            return ns
        print(cities)
        print(list(map(f, cities)), '\n')

    f2()

    def f3():
        cities = ['London', 'Beijing', 'Kiev']
        print(cities)
        print(list(map(f, cities)), '\n')

    f3()

f1()

print(cities)
print(list(map(f, cities)), '\n')
