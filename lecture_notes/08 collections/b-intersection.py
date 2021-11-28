def intersection(list1, list2):
    result = []

    for item in list1:
        if item in list2:
            result.append(item)
    return result


def fast_intersection(list1, list2):
    return list(set(list1) & set(list2))


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print(f'cities1: {cities1}, cities2: {cities2}')

intersection_result = intersection(cities1, cities2)
fast_intersection_result = fast_intersection(cities1, cities2)
print(f'intersection: {intersection_result}')
print(f'fast intersection: {fast_intersection_result}')
