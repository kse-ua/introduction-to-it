cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda x: len(x)

def upper_cities():
    old_cities = ['Athens', 'Roma']
    f_1 = lambda x: x.upper()
    print({'cities': old_cities})
    print(list(map(f_1, old_cities)))
upper_cities()

def lower_cities():
    old_cities = ['Athens', 'Roma']
    f_2 = lambda x: x.lower()
    print({'cities': old_cities})
    print(list(map(f_2, old_cities)))
lower_cities()


def last_cities():
    new_cities = ['London', 'Beijing', 'Kiev']
    f_3 = lambda x: x.upper()
    print({'cities': new_cities})
    print(list(map(f_3, new_cities)))
last_cities()

print(cities)
print(list(map(f, cities)))
