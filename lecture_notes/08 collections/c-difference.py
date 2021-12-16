def difference(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)
    return result


def fast_difference(list1, list2):
    return list(set(list1) - set(list2))


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
difference_result = difference(cities1, cities2)
fast_difference_result = fast_difference(cities1, cities2)

print(f'cities1: {cities1}, cities2: {cities2}')
print(f'difference: {difference_result}')
print(f'fast difference: {fast_difference_result}')
