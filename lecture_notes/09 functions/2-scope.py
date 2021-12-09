cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s : len(s)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s : s.upper()

    print(cities)
    # result = map(f, cities)
    print([f(x) for x in cities])
    
    f = lambda s : s.lower()
    print([f(x) for x in cities])


    def another(): 
        cities = ['London', 'Beijing', 'Kiev']
        print([f(x) for x in cities]) # how to get the first upper func

    another()

    print(map(another, cities))  # why it is not working???

f1()
print(cities)
print([f(x) for x in cities])
