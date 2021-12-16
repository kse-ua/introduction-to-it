def difference(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)
    return result


def complement(list1, list2):
    return difference(list2, list1)


def fast_complement(list1, list2):
    return list(set(list2) - set(list1))


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print(f'cities1: {cities1}, cities2: {cities2}')

complement_result = complement(cities1, cities2)
fast_complement_result = fast_complement(cities1, cities2)
print(f'complement: {complement_result}')
print(f'fast complement: {fast_complement_result}')
