cities = ['Athens', 'Roma',
 'London', 'Beijing', 'Kiev', 'Riga']
def f(s):
    return len(s)

def f1():
    cities = ['Athens', 'Roma']
    def f_u(s): 
      return s.upper()
    pr = map(f_u, cities)
    print(list(pr))  
    # listToStr = ' '.join([str(elem) for elem in cities])
    def f_l(s):
        return s.lower()
    pr = map(f_l, cities)
    print(list(pr))  
    cities = ['London', 'Beijing', 'Kiev']
    pr = map(f_u, cities)
    print(list(pr))  


f1()
print(f(cities))
