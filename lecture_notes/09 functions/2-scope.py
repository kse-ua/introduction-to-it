cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s : len(s)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s : s.upper()

    print(cities)
    # result = map(f, cities)
    print(list(map(f, cities)))
    
    f = lambda s : s.lower()
    print(list(map(f, cities)))

    def another(): 
        cities = ['London', 'Beijing', 'Kiev']
        print(list(map(f, cities))) # how to get the first upper func

    another()

f1()
print(cities)
print(list(map(f, cities)))
