cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
counting_length = lambda city: len(city)


def to_upper_case():
    cities = ['Athens', 'Roma']
    function = lambda element: element.upper()
    print(cities)
    big_letter_cities = map(function, cities)
    print(list(big_letter_cities))
to_upper_case()


def to_lower_case():
    cities = ['Athens', 'Roma']
    new_function = lambda city_from_cities: city_from_cities.lower()
    print(cities)
    small_letter_cities = map(new_function, cities)
    print(list(small_letter_cities))
to_lower_case()


def for_other_cities():
    new_list_cities = ['London', 'Beijing', 'Kiev']
    func = lambda city: city.upper()
    print(new_list_cities)
    print(list(map(func, new_list_cities)))
for_other_cities()

print(cities)
cities_length = map(counting_length, cities)
print(list(cities_length))
