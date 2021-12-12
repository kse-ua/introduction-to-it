cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']


def count_length_worlds(cities):
    return [len(city) for city in cities]


def to_lower_case(any_list):
    cities = ['Athens', 'Roma']
    for city in range(len(any_list)):
        any_list[city] = any_list[city].lower()
    return any_list


def to_upper_case(any_list):
    for city in range(len(any_list)):
        any_list[city] = any_list[city].upper()
    return any_list


print(to_upper_case(['Athens', 'Roma']))
print(to_lower_case(['Athens', 'Roma']))
print(to_upper_case(['London', 'Beijing', 'Kiev']))
print(cities)
print(count_length_worlds(cities))
