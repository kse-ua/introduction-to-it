cache = {}


def add_procedure(a, b):
    key = f'{a}, {b}'
    if cache.get(key):
        return cache[key]
    res = a + b
    cache[key] = res
    return res


def sub_procedure(a, b):
    key = f'{a}, {b}'
    if cache.get(key):
        return cache[key]
    res = a - b
    cache[key] = res
    return res


print({"sub": sub_procedure(5, 2)})
print({"add": add_procedure(5, 2)})