cache = {}


def add_procedure(a, b):
    key = f'{a}, {b}'
    res = a + b
    cache[key] = res
    return res


def sub_procedure(a, b):
    key = f'{a}, {b}'
    res = a - b
    cache[key] = res
    return res


print('sub_procedure:', sub_procedure(5, 2))
print('add_procedure:', add_procedure(5, 2))

