from typing import Final

cities = {'Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga'}
f = lambda s : len(s)

def f1():
    cities: Final = {'Athens', 'Roma'}
    f: Final = lambda s: s.upper()
    print(list(map(f,cities)))

    f: Final = lambda s: s.lower()
    print(list(map(f,cities)))

    cities: Final = {'London', 'Beijing', 'Kiev'}
    f: Final = lambda s: s.count('n')

    print(list(map(f,cities)))

f1()
