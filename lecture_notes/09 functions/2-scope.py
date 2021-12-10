cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s: len(s) 

def func():
    cities = ['Athens', 'Roma']
    f = lambda s: s.upper()
    
    print('{cities: ' + str(cities) + '}')
    print(map(f, cities ))


    def func_1():
        f = lambda s: s.lower()

        print('{cities: ' + str(cities) + '}')
        print(map(f, cities ))
    func_1()

    def func_2():
        cities = ['London', 'Beijing', 'Kiev']
        
        print('{cities: ' + str(cities) + '}')
        print(map(f, cities ))
    func_2()
func()   

print('{cities: ' + str(cities) + '}')
print(map(f,cities ))
