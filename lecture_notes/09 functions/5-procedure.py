add_function = lambda a, b: a + b
cache = {}

def add_procedure(a, b):
    key = f'{a}, {b}'
    res = a + b
    cache[key] = res
    return res


print([
    add_function(10, 20),
    add_function(1, 2),
    add_function(100, 20),
    add_function(100, 200)
])

print([
    add_procedure(10, 20),
    add_procedure(1, 2),
    add_procedure(100, 20),
    add_procedure(100, 200)
])
