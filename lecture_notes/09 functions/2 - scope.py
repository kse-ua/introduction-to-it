cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']


def to_upper_case(list):
    for city in range(len(list)):
        list[city] = list[city].upper()
    return list


print(['Athens', 'Roma'])
print(to_upper_case(['Athens', 'Roma']))


def to_lower_case(list):
    for city in range(len(list)):
        list[city] = list[city].lower()
    return list


print(['Athens', 'Roma'])
print(to_lower_case(['Athens', 'Roma']))

print(['London', 'Beijing', 'Kiev'])
print(to_upper_case(['London', 'Beijing', 'Kiev']))


def count_len(cities):
    return [len(city) for city in cities]


print(cities)
print(count_len(cities))
