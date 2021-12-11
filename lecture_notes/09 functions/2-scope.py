cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
cities_length = list(map(lambda city: len(city), cities))


def transform():
    cities = ['Athens', 'Roma']

    upper_cities = list(map(lambda to_upper: to_upper.upper(), cities))
    print(cities)
    print(upper_cities)

    lower_cities = list(map(lambda to_lower: to_lower.lower(), cities))
    print(cities)
    print(lower_cities)

    cities = ['London', 'Beijing', 'Kiev']
    upper_cities = list(map(lambda to_upper: to_upper.upper(), cities))

    print(cities)
    print(upper_cities)

transform()

print(cities)
print(cities_length)
