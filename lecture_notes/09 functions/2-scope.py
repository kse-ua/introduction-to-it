cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = list(map(lambda x: len(x), cities))


def f1():
    cities = ['Athens', 'Roma']
    f = list(map(lambda x: x.upper(), cities))

    print({'cities': cities})
    print(f)

    f = list(map(lambda x: x.lower(), cities))

    print({'cities': cities})
    print(f)

    cities = ['London', 'Beijing', 'Kiev']
    f = list(map(lambda x: x.upper(), cities))

    print({'cities': cities})
    print(f)


f1()

print({'cities': cities})
print(list(f))
