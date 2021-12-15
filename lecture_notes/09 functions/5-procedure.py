def add_function(a, b):
    res = a + b
    return res


cache = {}


def add_procedure(a, b):
    global cache
    key = str(a) + ', ' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res


print([
add_function(10, 20),
add_function(1, 2),
add_function(100, 20),
add_function(100, 200),
])


print([
add_procedure(10, 20),
add_procedure(1, 2),
add_procedure(100, 20),
add_procedure(100, 200),
])


