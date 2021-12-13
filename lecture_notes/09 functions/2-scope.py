cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']

# I have renamed some of the variables for clarity while keeping those that demonstarate the idea of scopes
length_measurement = lambda s: len(s)


def teaching_scopes():
    cities = ['Athens', 'Roma']
    upper_casing = lambda s: s.upper()

    print({'cities': cities})
    print(list(map(upper_casing, cities)))

    # since py isn't able to work with scopes in the way that js can we will redefine "cities" again to have same effect
    cities = ['Athens', 'Roma']
    lower_casing = lambda s: s.lower()
    print({'cities': cities})
    print(list(map(lower_casing, cities)))

    # and once again
    cities = ['London', 'Beijing', 'Kiev']
    print({'cities': cities})
    print(list(map(upper_casing, cities)))


teaching_scopes()
print({'cities': cities})
print(list(map(length_measurement, cities)))
