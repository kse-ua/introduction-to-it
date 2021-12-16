cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = list(map(lambda x: len(x), cities))


def upper_cities():
    old_cities = ['Athens', 'Roma']
    f_1 = list(map(lambda x: x.upper(), old_cities))
    print({'cities': old_cities})
    print(f_1)


upper_cities()


def lower_cities():
    old_cities = ['Athens', 'Roma']
    f_2 = list(map(lambda x: x.lower(), old_cities))
    print({'cities': old_cities})
    print(f_2)


lower_cities()


def last_cities():
    new_cities = ['London', 'Beijing', 'Kiev']
    f_3 = list(map(lambda x: x.upper(), new_cities))
    print({'cities': new_cities})
    print(f_3)


last_cities()


print(cities)
print(f)
