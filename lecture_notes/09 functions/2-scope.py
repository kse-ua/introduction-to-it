cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s: len(s) 

def f1():
    cities = ['Athens', 'Roma']
    f = lambda s: s.upper()
    
    print('{cities: ' + str(cities) + '}')
    print(map(f, cities ))


    def f1_1():
        f = lambda s: s.lower()

        print('{cities: ' + str(cities) + '}')
        print(map(f, cities ))
    f1_1()

    def f1_2():
        cities = ['London', 'Beijing', 'Kiev']
        
        print('{cities: ' + str(cities) + '}')
        print(map(f, cities ))
    f1_2()
f1()   

print('{cities: ' + str(cities) + '}')
print(map(f,cities ))