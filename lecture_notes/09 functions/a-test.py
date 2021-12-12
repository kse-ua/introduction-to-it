cache = {}


def add_procedure(a, b):
    key = f'{a}, {b}'
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res


def sub_procedure(a, b):
    key = f'{a}, {b}'
    if key in cache:
        return cache[key]
    res = a - b
    cache[key] = res
    return res


def test(f, args, res):
    result = f(*args)
    if result == res:
        return True
    else:
        return False


print([
    test(add_procedure, [1, 2], 3),
    test(add_procedure, [100, 20], 120),
    test(add_procedure, [100, 200], 300),
    test(sub_procedure, [5, 2], 3),
    test(add_procedure, [5, 2], 7)
])
