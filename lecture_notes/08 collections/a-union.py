def union(list1, list2):
    united = list1[:]

    for item in list2:
        if item not in united:
            united.append(item)

    return united


def fast_union(list1, list2):
    return list(set(list1 + list2))


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
union_result = union(cities1, cities2)
fast_union_result = fast_union(cities1, cities2)

print(f'cities1: {cities1}, cities2: {cities2}')
print(f'union: {union_result}')
print(f'fast union: {fast_union_result}')
