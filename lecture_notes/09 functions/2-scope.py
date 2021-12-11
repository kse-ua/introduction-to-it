cities = ['Athens', 'Roma',
 'London', 'Beijing', 'Kiev', 'Riga']
def f(s):
    return len(s)

def f1():
    cities = ['Athens', 'Roma']
    def f(s): 
      return s.upper()
    print(cities)
    pr = map(f, cities)
    print(list(pr))  
    # listToStr = ' '.join([str(elem) for elem in cities])
    def f(s):
        return s.lower()
    pr = map(f, cities)
    print(list(pr))  
    cities = ['London', 'Beijing', 'Kiev']
    print(cities)
    pr = map(f, cities)
    print(list(pr))  



f1()
print(cities)
print(f(cities))
